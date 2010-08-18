#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="OpenJPEG_v1_3"

def setup():
    shelltools.system("rm -rf jp3d libs")

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DBUILD_EXAMPLES:BOOL=ON \
                          -DBUILD_SHARED_LIBS:BOOL=ON \
                          -DINCLUDE_INSTALL_DIR=/%s/include" % get.defaultprefixDIR(), sourceDir="..")


def build():
    autotools.make("-C build")

def install():
    autotools.rawInstall("DESTDIR=%s -C build" % get.installDIR())

    pisitools.dosym("openjpeg/openjpeg.h", "/usr/include/openjpeg.h")

    pisitools.dodoc("ChangeLog", "README.linux", "license.txt")
