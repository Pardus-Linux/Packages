#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

NoStrip = ["/"]
WorkDir = "coolplug"

def build():
    autotools.make("CC=dietlibc-gcc")

def install():
    pisitools.dosbin("coolplug", "/sbin")
