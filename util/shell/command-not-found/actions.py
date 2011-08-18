#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dobin("src/command-not-found")

    pisitools.insinto("/var/db/command-not-found", "data/packages-%s.db" % get.ARCH(), "packages.db")

    for lang in ["da", "de", "es", "fr", "hu", "it", "nl", "ru", "sv", "tr"]:
        pisitools.domo("po/%s.po" % lang, lang, "command-not-found.mo")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
