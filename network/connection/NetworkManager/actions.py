#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

#WorkDir = "%s-0.8" % get.srcNAME()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-more-warnings \
                         --localstatedir=/var \
                         --with-crypto=nss \
                         --with-distro=pardus \
                         --with-resolvconf=/etc/resolv.conf \
                         --with-system-ca-path=/etc/ssl/certs \
                         --with-tests")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/NetworkManager")
    pisitools.dodir("/etc/NetworkManager/VPN")
    pisitools.dodir("/etc/NetworkManager/system-connections")

    pisitools.dodoc("README", "COPYING")
