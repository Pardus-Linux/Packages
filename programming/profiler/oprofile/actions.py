#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    for i in ["AUTHORS", "NEWS"]:
        shelltools.touch(i)

    autotools.autoreconf("-fi")
    autotools.configure("--with-kernel-support \
                         --with-separate-debug-dir=/usr/lib/debug \
                         --with-qt-dir=/void \
                         --enable-abi \
                         --enable-static=no \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "TODO", "AUTHORS", "COPYING", "ChangeLog*")
