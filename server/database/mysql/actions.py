#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    # Export flags
    shelltools.export("CFLAGS", "%s -DHAVE_ERRNO_AS_DEFINE=1 -fPIC" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s \
                                     -felide-constructors \
                                     -fno-exceptions \
                                     -fno-rtti \
                                     -fno-implicit-templates -fPIC" % get.CXXFLAGS())

    # Configure!
    autotools.configure("--libexecdir=/usr/sbin \
                         --sysconfdir=/etc/mysql \
                         --localstatedir=/var/lib/mysql \
                         --with-low-memory \
                         --enable-local-infile \
                         --with-mysqld-user=mysql \
                         --with-client-ldflags=-lstdc++ \
                         --enable-thread-safe-client \
                         --with-comment=\"Pardus Linux\" \
                         --with-unix-socket-path=/var/run/mysqld/mysqld.sock \
                         --without-docs \
                         --enable-shared \
                         --without-readline \
                         --disable-static \
                         --without-libwrap \
                         --with-ssl=/usr \
                         --without-debug \
                         --with-charset=utf8 \
                         --with-collation=utf8_general_ci \
                         --with-extra-charsets=all \
                         --with-geometry \
                         --with-big-tables \
                         --enable-assembler \
                         --with-plugins=innobase \
                         --with-embedded-server")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s benchdir_root=\"/usr/share/mysql\"" % get.installDIR())

    # Extra headers
    pisitools.insinto("/usr/include/mysql", "include/my_config.h")
    pisitools.insinto("/usr/include/mysql", "include/my_dir.h")

    # Links
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlanalyze")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlrepair")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqloptimize")

    # Cleanup
    pisitools.remove("/usr/share/mysql/mysql.server")
    pisitools.remove("/usr/share/mysql/binary-configure")
    pisitools.remove("/usr/share/mysql/mysql-log-rotate")
    pisitools.remove("/usr/share/mysql/mi_test*")
    pisitools.remove("/usr/share/mysql/my-*.cnf")
    pisitools.remove("/usr/share/mysql/config.*")
    pisitools.removeDir("/usr/share/aclocal")

    # Move libs to /usr/lib
    pisitools.domove("/usr/lib/mysql/libmysqlclient*.so*", "/usr/lib")

    # Links to libs
    pisitools.dosym("../libmysqlclient.so", "/usr/lib/mysql/libmysqlclient.so")
    pisitools.dosym("../libmysqlclient_r.so", "/usr/lib/mysql/libmysqlclient_r.so")

    # No tests, benchs
    pisitools.removeDir("/usr/mysql-test")
    pisitools.removeDir("/usr/share/mysql/sql-bench")

    # Config
    pisitools.insinto("/etc/mysql", "scripts/mysqlaccess.conf")

    # Data dir
    pisitools.dodir("/var/lib/mysql")

    # Logs
    pisitools.dodir("/var/log/mysql")
    shelltools.touch("%s/var/log/mysql/mysql.log" % get.installDIR())
    shelltools.touch("%s/var/log/mysql/mysql.err" % get.installDIR())
    pisitools.dodir("/var/lib/mysql/innodb")

    # Runtime data
    pisitools.dodir("/var/run/mysqld")

    # Documents
    pisitools.dodoc("README", "COPYING", "ChangeLog", "EXCEPTIONS-CLIENT")
    pisitools.dodoc("support-files/my-*.cnf")
