#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-doc \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")
