#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-network \
                         --enable-serial \
                         --enable-input \
                         --enable-audio \
                         --enable-service \
                         --enable-gstreamer \
                         --enable-alsa \
                         --enable-usb \
                         --enable-netlink \
                         --enable-tools \
                         --enable-bccmd \
                         --enable-dfutool \
                         --enable-cups \
                         --enable-hidd \
                         --enable-dund \
                         --enable-pand \
                         --enable-test \
                         --enable-pcmcia \
                         --enable-configfiles \
                         --with-systemdsystemunitdir=/lib/systemd/system \
                         --with-ouifile=/usr/share/misc/oui.txt \
                         --disable-hid2hci \
                         --libexecdir=/lib \
                         --localstatedir=/var")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install oui file
    pisitools.insinto("/usr/share/misc", "oui.txt")

    # Install conf files
    for i in ["audio", "input", "network"]:
        pisitools.insinto("/etc/bluetooth", "%s/%s.conf" % (i,i))

    # Simple test tools
    for i in ["simple-agent", "simple-service", "monitor-bluetooth",
              "list-devices", "apitest", "hsmicro", "hsplay",
              "test-adapter", "test-device", "test-discovery",
              "test-manager", "test-serial", "test-service",
              "test-telephony", "hstest", "attest", "sdptest",
              "scotest"]:
        pisitools.dobin("test/%s" % i)

    # Additional tools
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")

    # Install documents
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
