#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    for i in ["base", "dicts"]:
        pisitools.insinto("/usr/share/texmf-site/tex/latex/%s" % get.srcNAME(), "%s/*" % i)
        pisitools.dodoc("ChangeLog", "README", "doc/English/*")

