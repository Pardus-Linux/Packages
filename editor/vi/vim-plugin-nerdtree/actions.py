#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    for folder in ["plugin", "doc", "nerdtree_plugin"]:
        pisitools.insinto("/usr/share/vim/vimfiles/", folder)

    pisitools.dodoc("license.txt")
