#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sabishape-%s" % get.srcVERSION().replace("2.2_20", "")

def install():
    for i in ["sabishape", "sabishaperc"]:
        pisitools.dosbin(i)

    for i in ["sabishape.8", "sabishaperc.5"]:
        pisitools.doman(i)

