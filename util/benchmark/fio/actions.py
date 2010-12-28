#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("CC='%s' EXTFLAGS='%s' V=1" % (get.CC(), get.CFLAGS()))

def install():
    autotools.install()

    pisitools.dodoc("README", "HOWTO", "COPYING")

    pisitools.dodir("/%s/fio/examples" % get.docDIR())
    pisitools.insinto("/%s/fio/examples" % get.docDIR(), "examples/*")
