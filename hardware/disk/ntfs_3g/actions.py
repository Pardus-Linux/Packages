#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.configure("--disable-static \
                         --disable-ldconfig \
                         --sbindir=/sbin \
                         --bindir=/bin \
                         --libdir=/usr/lib \
                         --docdir=/usr/share/doc/%s" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/pkgconfig", "libntfs-3g/*.pc")

    # Create some compat symlinks

    pisitools.dosym("mount.ntfs-3g", "/sbin/mount.ntfs-fuse")
    pisitools.dosym("mount.ntfs-3g", "/sbin/mount.ntfs")
    pisitools.dosym("ntfs-3g", "/bin/ntfsmount")

    pisitools.dosym("/bin/ntfs-3g", "/usr/bin/ntfs-3g")
    pisitools.dosym("/bin/ntfsmount", "/usr/bin/ntfsmount")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "NEWS", "README")
