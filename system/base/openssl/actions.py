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
                       --libdir=lib \
                       --openssldir=/etc/pki/tls \
                       --enginesdir=/usr/lib/openssl/engines \
                       zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
                       enable-cms enable-md2 threads shared -Wa,--noexecstack")

    pisitools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
    pisitools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    autotools.make("depend")
    autotools.make("-j1")
    autotools.make("rehash")

def check():
    #FIXME: Some tests write into /etc/pki directory which violates
    # sandbox rules. It is not important for now. However, we will
    # need to fix it later. (08/17/2010 --Eren)
    homeDir = "%s/test-home" % get.workDIR()
    shelltools.export("HOME", homeDir)
    shelltools.makedirs(homeDir)

    autotools.make("-j1 test")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())

    # Move engines to /usr/lib/openssl/engines
    pisitools.dodir("/usr/lib/openssl")
    pisitools.domove("/usr/lib/engines", "/usr/lib/openssl")

    # Certificate stuff
    pisitools.dobin("tools/c_rehash")
    pisitools.dosym("/etc/pki/tls/certs/ca-bundle.crt","/etc/pki/tls/cert.pem")

    # Rename conflicting manpages
    pisitools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
    pisitools.rename("/usr/share/man/man3/rand.3", "ssl-rand.3")
    pisitools.rename("/usr/share/man/man3/err.3", "ssl-err.3")

    # Create CA dirs
    for cadir in ["CA", "CA/private", "CA/certs", "CA/crl", "CA/newcerts"]:
        pisitools.dodir("/etc/pki/%s" % cadir)

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
