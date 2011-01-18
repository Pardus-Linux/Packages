#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/php5/smarty/", "libs/*")

    pisitools.dodoc("COPYING.lib", "SMARTY2_BC_NOTES",  "README")
