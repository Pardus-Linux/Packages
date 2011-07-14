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

def setup():
    def cleanup():
        for p in ("config.*", "ltconfig", "ltmain.sh", "libtool.m4"):
            shelltools.unlink("config/%s" % p)

    cleanup()
    autotools.autoreconf("-vfi --no-recursive -I config -I cmulocal")
    shelltools.cd("saslauthd")
    cleanup()
    autotools.autoreconf("-vi --no-recursive -I config -I ../cmulocal -I ../config")
    shelltools.cd("..")

    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    autotools.configure("--with-saslauthd=/var/run/saslauthd \
                         --with-pwcheck=/var/lib/sasl2 \
                         --with-configdir=/etc/sasl2 \
                         --with-plugindir=/usr/lib/sasl2 \
                         --with-dbpath=/etc/sasl2/sasldb2 \
                         --enable-login \
                         --enable-ntlm \
                         --enable-auth-sasldb \
                         --disable-krb4 \
                         --disable-otp \
                         --disable-static \
                         --with-openssl \
                         --with-pam \
                         --disable-gssapi \
                         --without-mysql \
                         --disable-mysql \
                         --without-pgsql \
                         --disable-postgres \
                         --disable-java \
                         --disable-sql \
                         --with-devrandom=/dev/urandom \
                         --with-dblib=gdbm")

def build():
    autotools.make("-j1")
    autotools.make("-C saslauthd testsaslauthd")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C plugins" % get.installDIR())

    pisitools.dodir("/etc/sasl2")
    pisitools.dodir("/var/run/saslauthd")

    for doc in ["AUTHORS", "COPYING", "ChangeLog", "LDAP_SASLAUTHD", "NEWS", "README"]:
        pisitools.newdoc("saslauthd/%s" % doc, "saslauthd/%s" % doc)

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "doc/TODO", "doc/*.txt")
