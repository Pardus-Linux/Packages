#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cryptsetup-%s" % get.srcVERSION()

def setup():
    # Libs should be installed to /lib because it's possible that /usr
    # is on a different partition other than rootfs.
    # See: http://cvs.fedoraproject.org/viewvc/devel/cryptsetup-luks/cryptsetup-luks.spec?view=co
    autotools.configure("--sbindir=/sbin")
    pisitools.dosed("lib/Makefile", "-lgpg-error", "")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.remove("/usr/lib/libcryptsetup.la")

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS", "TODO")
