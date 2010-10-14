#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    # No need to package test programs
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS*", "README*", "RELEASE*", "todo*")
