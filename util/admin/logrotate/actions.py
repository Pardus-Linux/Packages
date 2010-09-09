#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\"" % get.CFLAGS())

def install():
    autotools.rawInstall("PREFIX=%s MANDIR=%s" % (get.installDIR(), get.manDIR()))

    pisitools.dodir("/etc/logrotate.d")
    pisitools.dodir("/var/lib")

    pisitools.insinto("/etc/cron.daily", "examples/logrotate.cron")
    pisitools.insinto("/etc", "examples/logrotate-default", "logrotate.conf")

    pisitools.dodoc("CHANGES", "COPYING", "README*")
