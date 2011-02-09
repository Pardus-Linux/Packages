# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-gnome-vfs \
                         --disable-ntfsmount")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove not shipped binaries man pages
    pisitools.remove("/usr/share/man/man8/ntfsmount.8")
    pisitools.remove("/usr/share/man/man8/libntfs-gnomevfs.8")

    pisitools.dodoc("ChangeLog", "AUTHORS", "CREDITS", "NEWS", "README*")
