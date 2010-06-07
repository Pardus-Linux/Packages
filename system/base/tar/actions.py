#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-backup-scripts \
                         --bindir=/bin \
                         --libexecdir=/usr/sbin \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/sbin/backup","backup-tar")
    pisitools.rename("/usr/sbin/restore","restore-tar")

    pisitools.dosym("/usr/sbin/rmt", "/etc/rmt")

    pisitools.doman("doc/tar.1")
    pisitools.doman("doc/rmt.8")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS")

def check():
    autotools.make("check")
