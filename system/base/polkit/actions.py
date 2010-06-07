#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-pam-module-dir=/lib/security/ \
                         --with-os-type=Pardus \
                         --enable-examples \
                         --localstatedir=/var \
                         --libexecdir=/usr/libexec/polkit-1 \
                         --disable-introspection \
                         --disable-man-pages \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/var/lib/polkit-1")
    shelltools.chmod("%s/var/lib/polkit-1" % get.installDIR(), mode=00700)
    shelltools.chmod("%s/etc/polkit-1/localauthority" % get.installDIR(), mode=00700)

    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING", "COPYING")
