#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION())

shelltools.export("HOME", get.workDIR())

def setup():
    # Remove after switching to new KDEPIM 4.6 tree
    # We already have those translations in kdepim-4.4 package
    pisitools.dosed("messages/CMakeLists.txt", "add_subdirectory\\(kdepim\\-runtime\\)", "#add_subdirectory(kdepim-runtime)")
    pisitools.dosed("messages/CMakeLists.txt", "add_subdirectory\\(kdepim\\)", "#add_subdirectory(kdepim)")

    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

