#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf() # have a buggy mktime check
    autotools.configure("--bindir=/bin \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned binaries
    pisitools.remove("/bin/*-*")

    pisitools.dosym("gawk.1", "/usr/share/man/man1/awk.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "LIMITATIONS", "NEWS", "PROBLEMS", "README")
