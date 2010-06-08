#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--exec-prefix= \
                         --libexecdir=/lib/udev \
                         --libdir=/usr/lib \
                         --disable-introspection \
                         --enable-logging")

def build():
    autotools.make("all")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # This were explicitly not installed in Pardus 2008, so I remove it.
    pisitools.remove("/lib/udev/rules.d/79-fstab_import.rules")

    # FIXME: We have GROUP conversions here!
    # Only some gentoo and 50-udev-default.rules are affected by the renamings below

    pisitools.dosed("%s/lib/udev/rules.d/60-floppy.rules" % get.installDIR(), '-G floppy', '-G pnp')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="floppy"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="lp"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="cdrom"', 'GROUP="removable"')

    # create needed directories
    for d in ("", "net", "pts", "shm", "hugepages"):
        pisitools.dodir("/lib/udev/devices/%s" % d)

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    # Remove gtk-doc
    pisitools.removeDir("/usr/share/gtk-doc")

    # Install docs
    pisitools.dodoc("COPYING", "ChangeLog", "README", "TODO")
