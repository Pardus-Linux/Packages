#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    #install HAL file for portable audio players
    pisitools.insinto("/usr/share/hal/fdi/information/20thirdparty", "libmtp.fdi", "10-libmtp.fdi")

    # Regenerate udev rules without MODE= property
    shelltools.system('examples/hotplug -a\'SYMLINK+="libmtp-%k" ENV{ACL_MANAGE}="0" TAG+="udev-acl"\' > libmtp.rules')

    #install UDEV rules
    pisitools.insinto("/lib/udev/rules.d/", "libmtp.rules", "65-mtp.rules")

    pisitools.removeDir("/usr/share/doc/libmtp-*")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
