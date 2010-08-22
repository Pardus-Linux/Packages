#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE \
                          -DCLUCENE_LIBRARY_DIR=/usr/include \
                          -DENABLE_FAM=ON \
                          -DENABLE_POLLING=ON \
                          -DENABLE_INOTIFY=ON ", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../")
    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")
