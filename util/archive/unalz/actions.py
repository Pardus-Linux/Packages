#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "unalz"

def build():
    autotools.make("linux-utf8")

def install():
    pisitools.dobin('unalz')
    pisitools.dodoc("readme.txt")

