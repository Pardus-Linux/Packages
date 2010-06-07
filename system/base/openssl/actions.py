#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./config \
                       --prefix=/usr \
                       --openssldir=/etc/ssl \
                       zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
                       threads shared -Wa,--noexecstack")

    pisitools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
    pisitools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    autotools.make("depend")
    autotools.make("-j1")
    autotools.make("rehash")

def check():
    homeDir = "%s/test-home" % get.workDIR()
    shelltools.export("HOME", homeDir)
    shelltools.makedirs(homeDir)

    autotools.make("-j1 test")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())

    # Certificate stuff
    pisitools.dobin("tools/c_rehash")
    pisitools.dosym("/etc/ssl/certs/ca-bundle.crt","/etc/ssl/cert.pem")

    # Rename conflicting manpages
    pisitools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
    pisitools.rename("/usr/share/man/man3/rand.3", "ssl-rand.3")
    pisitools.rename("/usr/share/man/man3/err.3", "ssl-err.3")

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
