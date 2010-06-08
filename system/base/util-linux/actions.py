#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="util-linux-ng-%s" % get.srcVERSION().replace("_","-")

def setup():
    shelltools.export("CFLAGS", "%s -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    shelltools.export("SUID_CFLAGS", "-fpie")
    shelltools.export("SUID_LDFLAGS", "-pie")
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf("-fi")
    autotools.configure('--bindir=/bin \
                         --sbindir=/sbin \
                         --enable-nls \
                         --enable-agetty \
                         --enable-cramfs \
                         --enable-mesg \
                         --enable-partx \
                         --enable-raw \
                         --enable-rdev \
                         --enable-rename \
                         --enable-schedutils \
                         --enable-write \
                         --enable-libuuid \
                         --enable-uuidd \
                         --with-audit \
                         --disable-switch_root \
                         --disable-fsck \
                         --disable-init \
                         --disable-kill \
                         --disable-last \
                         --disable-login-utils \
                         --disable-makeinstall-chown \
                         --disable-mesg \
                         --disable-reset \
                         --disable-rpath \
                         --disable-static \
                         --disable-use-tty-group \
                         --disable-wall')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "DEPRECATED", "README*", "TODO", "docs/*")
    pisitools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), "example.files")
