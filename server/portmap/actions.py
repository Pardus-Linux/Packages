#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "portmap_%s" % get.srcVERSION()

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    pisitools.dosbin("portmap", "/sbin")
    pisitools.dosbin("pmap_dump")
    pisitools.dosbin("pmap_set")

    pisitools.doman("portmap.8", "pmap_dump.8", "pmap_set.8")
    pisitools.dodoc("BLURBv5", "CHANGES", "README*")
