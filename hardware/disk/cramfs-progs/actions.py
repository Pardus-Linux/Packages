#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cramfs-%s" % get.srcVERSION()

def build():
    autotools.make()

def install():
    pisitools.dosbin("mkcramfs", "/sbin")
    pisitools.dosbin("cramfsck", "/sbin")
    pisitools.dodoc("README", "NOTES")
