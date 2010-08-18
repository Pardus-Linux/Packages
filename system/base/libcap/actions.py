#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Make.Rules", "^CFLAGS := .*$", "CFLAGS := %s" % get.CFLAGS())
    pisitools.dosed("Make.Rules", "^LDFLAGS := .*$", "LDFLAGS := %s" % get.LDFLAGS())

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    autotools.rawInstall("FAKEROOT=%s" % get.installDIR())

    pisitools.insinto("/etc/security", "pam_cap/capability.conf")

    # we should not need this static
    pisitools.remove("/lib/libcap.a")

    pisitools.dodoc("CHANGELOG", "README", "doc/capability.notes")
