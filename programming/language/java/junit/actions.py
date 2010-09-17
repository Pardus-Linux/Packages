#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="%s%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    shelltools.makedirs("src/main/java")
    shelltools.makedirs("src/test/java")
    shelltools.system("unzip junit-%s-src.jar -d src/main/java" % get.srcVERSION())

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant build jars")

def install():
    pisitools.insinto("/usr/share/java", "junit%s/junit-%s.jar" % (get.srcVERSION(), get.srcVERSION()), "junit.jar")

    pisitools.dohtml("cpl-v10.html", "README.html")
    pisitools.dodoc("doc/*.txt")
