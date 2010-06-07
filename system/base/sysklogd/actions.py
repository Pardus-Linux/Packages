#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("OS_CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    autotools.make()

def install():
    pisitools.dosbin("syslogd")
    pisitools.dosbin("klogd")
    pisitools.doman("*.[1-9]")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "MANIFEST", "NEWS", "README.1st", "README.linux")
