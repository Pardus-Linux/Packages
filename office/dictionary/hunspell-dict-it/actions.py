#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/hunspell", "*.dic")
    pisitools.insinto("/usr/share/hunspell", "*.aff")

    pisitools.dosym("/usr/share/hunspell/it_IT.dic", "/usr/share/hunspell/it_CH.dic")
    pisitools.dosym("/usr/share/hunspell/it_IT.aff", "/usr/share/hunspell/it_CH.aff")

    pisitools.dodoc("*.txt", "*AUTHORS", "*ChangeLog", "*COPYING")
