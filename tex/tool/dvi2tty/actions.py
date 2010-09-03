#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.dobin("dvi2tty")
    pisitools.dobin("disdvi")

    pisitools.doman("dvi2tty.1", "disdvi.1")

    pisitools.dodoc("COPYING", "README")
