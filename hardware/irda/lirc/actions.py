#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lirc-%s" % get.srcVERSION().replace("_", "")
ldflags = get.LDFLAGS().replace("-Wl,-O1", "")

def setup():
    shelltools.export("LDFLAGS", ldflags)
    autotools.autoreconf("-vfi")
    pisitools.dosed("configure*", "portaudio.h", "PORTAUDIO_DISABLED")

    autotools.configure("--localstatedir=/var \
                         --enable-sandboxed \
                         --enable-shared \
                         --disable-static \
                         --disable-debug \
                         --with-transmitter \
                         --with-x \
                         --with-port=0x3f8 \
                         --with-irq=4 \
                         --with-driver=userspace \
                         --with-syslog=LOG_DAEMON")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # needed for lircd pid
    pisitools.dodir("/var/run/lirc")

    # example configs
    pisitools.insinto("/etc", "contrib/lircd.conf", "lircd.conf")
    pisitools.insinto("/etc", "contrib/lircmd.conf", "lircmd.conf")

    pisitools.dohtml("doc/html/*.html")
    pisitools.rename("/%s/%s" % (get.docDIR(), get.srcNAME()), "lirc")

    pisitools.insinto("/%s/lirc/images" % get.docDIR(), "doc/images/*")
    pisitools.insinto("/%s/lirc/contrib" % get.docDIR(), "contrib/*")
    pisitools.insinto("/lib/udev/rules.d", "contrib/lirc.rules", "10-lirc.rules")

