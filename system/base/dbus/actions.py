#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-xml=expat \
                         --with-system-pid-file=/var/run/dbus/pid \
                         --with-system-socket=/var/run/dbus/system_bus_socket \
                         --with-session-socket-dir=/tmp \
                         --with-systemdsystemunitdir=/lib/systemd/system/ \
                         --with-dbus-user=dbus \
                         --localstatedir=/var \
                         --disable-selinux \
                         --disable-static \
                         --disable-tests \
                         --disable-asserts \
                         --disable-doxygen-docs \
                         --disable-xml-docs")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # needs to exist for the system socket
    pisitools.dodir("/var/run/dbus")
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/")
