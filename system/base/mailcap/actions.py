#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s sysconfdir=/%s mandir=/%s" % (get.installDIR(), get.confDIR(), get.manDIR()))

    pisitools.dodoc("COPYING", "NEWS")
