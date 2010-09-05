#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "microcode_ctl-%s" % get.srcVERSION()

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))


def install():
    pisitools.dosbin("microcode_ctl")

    pisitools.doman("microcode_ctl.8")
    pisitools.dodoc("Changelog","README")
