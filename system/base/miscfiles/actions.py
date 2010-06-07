#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())

    pisitools.dodoc("GNU*", "NEWS", "ORIGIN", "README", "dict-README")
