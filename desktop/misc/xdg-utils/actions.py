#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    # For fixing links' sandbox violations
    shelltools.export("HOME", get.workDIR())
    autotools.make("-C scripts scripts")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
