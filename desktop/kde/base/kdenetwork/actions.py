#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share"]

def setup():
    kde4.configure("-DWITH_JINGLE=TRUE")

def build():
    kde4.make()

def install():
    kde4.install()
