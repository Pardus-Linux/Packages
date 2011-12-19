#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--libexecdir=/usr/lib/dhcpcd \
                         --dbdir=/var/lib/dhcpcd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DBDIR=/var/lib/dhcpcd LIBEXECDIR=/usr/lib/dhcpcd DESTDIR=%s" % get.installDIR())

    # Remove hooks install the compat one
    pisitools.remove("/usr/lib/dhcpcd/dhcpcd-hooks/*")
    pisitools.insinto("/usr/lib/dhcpcd/dhcpcd-hooks", "dhcpcd-hooks/50-dhcpcd-compat")

    pisitools.dodoc("README")
