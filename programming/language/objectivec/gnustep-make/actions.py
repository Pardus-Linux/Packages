#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-config-file=/etc/GNUstep/GNUstep.conf \
                        --with-layout=fhs \
                        --enable-native-exceptions")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.makedirs("%s/etc/profile.d" % get.installDIR())
    shelltools.copy("GNUstep.sh", "%s/etc/profile.d/GNUstep.sh" % get.installDIR())

    pisitools.dodoc("FAQ", "README", "RELEASENOTES")
