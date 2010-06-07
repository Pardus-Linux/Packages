#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--sbindir=/sbin \
                         --with-apparmor \
                         --enable-gssapi-krb5=no \
                         --with-libwrap \
                         --without-prelude \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # remove RH specific bits
    pisitools.removeDir("/etc/sysconfig/")
    pisitools.removeDir("/etc/rc.d/")

    pythonmodules.fixCompiledPy()

    pisitools.dodir("/var/log/audit/")

    #disable zos-remote plugin to get rid of deps. like cyrus-sasl
    pisitools.remove("/usr/share/man/man8/audispd-zos-remote.8")
    pisitools.remove("/usr/share/man/man5/zos-remote.conf.5")

    pisitools.dodoc("AUTHORS", "ChangeLog", "THANKS", "TODO", "README", "COPYING")
