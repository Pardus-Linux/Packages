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

def setup():
    autotools.configure("--disable-static \
                         --disable-ldap \
                         --with-ssl \
                         --with-libidn \
                         --with-libssh2 \
                         --enable-threaded-resolver \
                         --enable-ipv6 \
                         --enable-http \
                         --enable-ftp \
                         --enable-gopher \
                         --enable-file \
                         --enable-dict \
                         --enable-manual \
                         --enable-telnet \
                         --enable-nonblocking \
                         --enable-largefile \
                         --with-ca-bundle=/etc/ssl/certs/ca-bundle.crt")

def build():
    autotools.make()

def check():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib" % get.curDIR())
    autotools.make("-C tests test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "docs/FEATURES", "docs/MANUAL", "docs/FAQ", "docs/BUGS")
