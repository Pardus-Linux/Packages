#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    autotools.configure("--enable-nls \
                         --disable-rpath")
                         # --enable-python \
                         # --enable-python-bindings \

def build():
    autotools.make()

# FIXME: python tests fail, others fail in 64bit, gentoo says tests are wrong
def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "BSD.txt", "GNU_GPL-2.0", "GNU_LGPL-2.0", "Artistic.txt")

