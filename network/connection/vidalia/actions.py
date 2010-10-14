#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure(installPrefix = "/%s" % (get.defaultprefixDIR()))

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("CHANGELOG", "CREDITS", "README", "README.*", "doc/version-spec.txt")
