#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # autoreconf is for under linking problem
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    shelltools.chmod("%s/usr/share/pygobject/xsl/fixxref.py" % get.installDIR(), 0755)
    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README")
