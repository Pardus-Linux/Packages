#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --with-ui \
                         --with-readline \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    for f in ("affixcompress", "makealias", "wordforms"):
        pisitools.dobin("src/tools/%s" % f)

    pisitools.dodoc("ABOUT-NLS", "AUTHORS*", "BUGS", "COPYING*", "NEWS", "README*", "THANKS", "TODO")
