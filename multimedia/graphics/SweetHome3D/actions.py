#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant")

def install():
    pisitools.insinto("/opt/SweetHome3D", "install/SweetHome3D-%s.jar" % get.srcVERSION())
