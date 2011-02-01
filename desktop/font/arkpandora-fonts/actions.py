#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/fonts/arkpandora/", "*.ttf")
    pisitools.insinto("/etc/fonts/conf.avail/", "local.conf.arkpandora", "62-arkpandora-fonts.conf")

    pisitools.dosym("../conf.avail/62-arkpandora-fonts.conf", "/etc/fonts/conf.d/62-arkpandora-fonts.conf")

    pisitools.dodoc("COPYRIGHT.TXT", "CHANGELOG.TXT")
