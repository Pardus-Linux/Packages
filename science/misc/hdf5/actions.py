#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_p", "-patch"))

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("--enable-cxx \
                         --enable-fortran \
                         --enable-production=no \
                         --disable-static \
                         --disable-parallel \
                         --with-pic")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ACKNOWLEDGMENTS", "COPYING", "README*", "release_docs/HISTORY-*", "release_docs/RELEASE.txt")
