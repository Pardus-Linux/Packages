#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--exec-prefix=\"\" \
               --sbindir=/sbin \
               --with-systemdsystemunitdir=/lib/systemd/system \
               --libdir=/usr/lib \
               --libexecdir=/lib/udev \
               --disable-introspection \
               --enable-logging"

    if get.buildTYPE() == "emul32":
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --libexecdir=/emul32/lib/udev \
                     --with-systemdsystemunitdir=/emul32/lib/systemd/system \
                     --datadir=/emul32/share \
                     --bindir=/emul32/bin \
                     --sbindir=/emul32/sbin \
                     --disable-extras"

    autotools.autoreconf("-fi")
    autotools.configure(options)

def build():
    autotools.make("all")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        return

    # create needed directories
    for d in ("", "net", "pts", "shm", "hugepages"):
        pisitools.dodir("/lib/udev/devices/%s" % d)

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    # Install docs
    pisitools.dodoc("COPYING", "ChangeLog", "README", "TODO", "extras/keymap/README.keymap.txt")
