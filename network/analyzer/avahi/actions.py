#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-mono \
                         --disable-qt3 \
                         --disable-qt4 \
                         --disable-doxygen-doc \
                         --disable-gtk \
                         --disable-gtk3 \
                         --disable-pygtk \
                         --disable-gobject \
                         --disable-python \
                         --disable-python-dbus \
                         --disable-glib \
                         --enable-autoipd \
                         --enable-core-docs \
                         --enable-shared \
                         --enable-compat-howl \
                         --enable-compat-libdns_sd \
                         --localstatedir=/var \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi \
                         --with-autoipd-group=avahi \
                         --with-avahi-priv-access-group=avahi")

    # Less invasive anti-rpath hack if one wants to avoid auto*foo
    pisitools.dosed("libtool", "hardcode_into_libs=yes", "hardcode_into_libs=no")

def build():
    # for mono sandbox errors
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    # for mono sandbox errors
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Add missing symlinks for avahi-compat-howl and avahi-compat-dns-sd
    pisitools.dosym("/usr/lib/pkgconfig/avahi-compat-howl.pc", "/usr/lib/pkgconfig/howl.pc")
    pisitools.dosym("/usr/lib/pkgconfig/avahi-compat-libdns_sd.pc", "/usr/lib/pkgconfig/libdns_sd.pc")
    pisitools.dosym("/usr/include/avahi-compat-libdns_sd/dns_sd.h", "/usr/include/dns_sd.h")

    # Remove unneded files and directory
    pisitools.removeDir("/var")
    pisitools.removeDir("/usr/lib/avahi")
    pisitools.removeDir("/usr/share/applications")

    # Remove example
    pisitools.remove("/etc/avahi/services/sftp-ssh.service")

    pisitools.dodoc("docs/AUTHORS","docs/README","docs/TODO")
