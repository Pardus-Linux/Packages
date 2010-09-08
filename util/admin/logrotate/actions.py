#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.dosbin("logrotate")
    pisitools.doman("logrotate.8")
    pisitools.dodir("/etc/logrotate.d")

    pisitools.dodoc("examples/logrotate*")
    pisitools.dodoc("CHANGES", "COPYING", "README*")
