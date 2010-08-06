#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.sym(".", "m4")
    shelltools.sym("LICENSE", "COPYING")
    for i in ["NEWS", "AUTHORS", "ChangeLog"]:
        shelltools.touch(i)

    pisitools.dosed("configure.in", "^ppl_minor_version=.*", "ppl_minor_version=11")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --with-ppl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
