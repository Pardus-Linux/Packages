#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():

    autotools.rawConfigure("-prefix /usr \
                            -bindir /usr/bin \
                            -libdir /usr/lib/ocaml \
                            -mandir /usr/share/man \
                            --with-pthread")

    pisitools.dosed("config/Makefile", "\(BYTECCCOMPOPTS=.*\)", "\1 %s" % (get.CFLAGS()))
    pisitools.dosed("config/Makefile", "\(NATIVECCCOMPOPTS=.*\)", "\1 %s" % (get.CFLAGS()))

def build():
    autotools.make("-j1 world")
    autotools.make("-j1 opt")
    autotools.make("-j1 opt.opt")

def install():
    autotools.rawInstall("BINDIR=%(install)s/usr/bin \
                          LIBDIR=%(install)s/usr/lib/ocaml \
                          MANDIR=%(install)s/usr/share/man" \
                          % { "install": get.installDIR()})

    pisitools.dodoc("Changes", "LICENSE", "README", "Upgrading")
