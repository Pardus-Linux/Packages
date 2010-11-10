#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --enable-more-warnings=yes \
                         --with-crypto=nss \
                         --with-distro=pardus \
                         --with-resolvconf=/etc/resolv.conf \
                         --with-system-ca-path=/etc/pki/tls/certs \
                         --with-tests")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("test/.libs/nm-online")

    pisitools.dodir("/var/lib/NetworkManager")
    pisitools.dodir("/etc/NetworkManager/VPN")
    pisitools.dodir("/etc/NetworkManager/system-connections")

    pisitools.dodoc("README", "COPYING")
