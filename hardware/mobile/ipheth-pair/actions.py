#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "ipheth"

def build():
    autotools.make("-C ipheth-pair/")

def install():
    pisitools.insinto("/usr/bin", "ipheth-pair/ipheth-pair")
    pisitools.insinto("/lib/udev/rules.d", "ipheth-pair/90-iphone-tether.rules")
