#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "b43-fwcutter-%s" % get.srcVERSION().replace(".", "")

def build():
    autotools.make()

def install():
    pisitools.dobin("b43-fwcutter")

    pisitools.dodoc("README")
    pisitools.doman("*.1")
