#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install" % get.installDIR())

