#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()
    cmaketools.make("doc")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/man/*/*")
    pisitools.dohtml("doc/html/*")

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README")
