#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "freeradius-server-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED -fPIC -DPIC" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie" % get.LDFLAGS())

    autotools.configure('--libdir=/usr/lib/freeradius \
                         --with-system-libtool \
                         --disable-ltdl-install \
                         --with-gnu-ld \
                         --with-threads \
                         --with-threads-pool \
                         --with-rlm-sql_postgresql-include-dir=/usr/include/pgsql \
                         --with-rlm-sql_postgresql-lib-dir=/usr/lib \
                         --with-rlm-sql_mysql-include-dir=/usr/include/mysql \
                         --with-rlm-sql_mysql-lib-dir=/usr/lib/mysql \
                         --with-unixodbc-lib-dir=/usr/lib \
                         --with-rlm-dbm-lib-dir=/usr/lib \
                         --with-rlm-krb5-include-dir=/usr/include/krb5 \
                         --with-modules="rlm_wimax" \
                         --without-rlm_eap_ikev2 \
                         --without-rlm_sql_iodbc \
                         --without-rlm_sql_firebird \
                         --without-rlm_sql_db2 \
                         --without-rlm_sql_oracle \
                         --without-rlm_eap_tnc \
                         --without-rlm_opendirectory \
                         --with-openssl-includes=/usr/include/openssl \
                         --enable-strict-dependencies \
                         --with-edir \
                         --with-udp-fromto \
                         --disable-static \
                         --with-pic')

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("R=%s" % get.installDIR())

    pisitools.dodir("/var/run/radiusd")
    pisitools.dodir("/var/lib/radiusd")
    pisitools.dodir("/var/log/radius/radacct")

    shelltools.touch("%s/var/log/radius/radutmp" % get.installDIR())
    shelltools.touch("%s/var/log/radius/radius.log" % get.installDIR())

    # remove useless init script
    pisitools.remove("/usr/sbin/rc.radiusd")

    pisitools.remove("/etc/raddb/experimental.conf")
    pisitools.removeDir("/etc/raddb/sql/mssql")
    pisitools.removeDir("/etc/raddb/sql/oracle")

    #pisitools.insinto("/usr/share/doc/freeradius/", "scripts")

    pisitools.dosed("%s/etc/raddb/radiusd.conf" % get.installDIR(), '^#user *= *radius', 'user = radiusd')
    pisitools.dosed("%s/etc/raddb/radiusd.conf" % get.installDIR(), '^#group *= *radius', 'group = radiusd')

    pisitools.dodoc("CREDITS", "README", "COPYRIGHT", "LICENSE", "todo/TODO")
