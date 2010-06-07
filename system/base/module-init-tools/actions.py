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

WorkDir = "module-init-tools-%s" % get.srcVERSION().replace("_", "-")

def setup():
    # Disable man pages
    pisitools.dosed("Makefile.am", "^dist_man_MANS = .*$", "")

    shelltools.export("CFLAGS", get.CFLAGS().replace("-O2", "-Os -g -DCONFIG_NO_BACKWARDS_COMPAT=1"))

    autotools.autoreconf("-fi")
    autotools.configure("--enable-zlib-dynamic --disable-static-utils")

def build():
    autotools.make()

def install():
    autotools.install("prefix=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
