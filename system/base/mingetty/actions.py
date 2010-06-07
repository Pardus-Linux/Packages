#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mingetty-1.0.7s"

def build():
    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    pisitools.dosbin("mingetty", "/sbin")
    pisitools.doman("mingetty.8")
    pisitools.insinto("/usr/share/locale/tr/LC_MESSAGES", "tr.mo", "mingetty.mo")

    pisitools.dodoc("ANNOUNCE", "COPYING", "TODO", "CHANGES")
