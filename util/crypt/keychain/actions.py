#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("keychain", "/usr/ucb:", "")

def install():
    pisitools.dobin("keychain")
    pisitools.dodoc("ChangeLog", "keychain.pod", "README")
    pisitools.doman("keychain.1")
