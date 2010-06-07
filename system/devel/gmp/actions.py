#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("CCAS","%s -c -Wa,--noexecstack" % get.CC())

    autotools.configure("--enable-cxx \
                         --disable-mpbsd \
                         --localstatedir=/var/state/gmp")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.doinfo("doc/*info*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LIB", "NEWS", "README")
