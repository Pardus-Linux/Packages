#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "static", "dynamic")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    autotools.install("ROOT=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "doc/*.txt")
