#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import Error

import os
from stat import *

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DWITH_examples=true \
                          -DWITH_demos=true \
                          -DWITH_GMPXX=ON \
                          -DWITH_CGAL_Qt3=OFF \
                          -DWITH_LEDA=OFF \
                          -DWITH_TAUCS=OFF", installPrefix="/usr",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make("-j1")

    # remove obsolote demos/examples that wont compile with new boost or qt
    obsolotes = ["demo/Periodic_3_triangulation_3", "demo/Polyhedron", "examples/BGL_arrangement_2",\
                 "examples/Ridges_3", "examples/BGL_polyhedron_3", "examples/Arrangement_on_surface_2",
                 "examples/Envelope_3", "examples/Surface_mesh_simplification", "examples/Jet_fitting_3",
                 "examples/Modular_arithmetic", "examples/Polynomial", "demo/Mesh_3", "examples/Mesh_3"]
    try:
        for i in obsolotes:
            shelltools.unlinkDir("%s" % i)
            shelltools.unlinkDir("%s/%s-%s/%s" % (get.workDIR(), get.srcNAME(), get.srcVERSION(), i))
    except Error, e:
        print e

    cmaketools.make("-j1 demos")
    cmaketools.make("-j1 examples")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/lib/CGAL")

    pisitools.dohtml("../doc_html/")

    pisitools.insinto("/usr/share/CGAL/examples", "../examples/*")

    # copy executables only
    for i in ["demo", "examples"]:
        for root, dirs, files in os.walk(i):
            for filename in files:
                curfile = os.path.join(root, filename)
                if os.stat(curfile)[ST_MODE] & S_IXUSR:
                    pisitools.insinto("/usr/share/CGAL/%s" % curfile, curfile)
