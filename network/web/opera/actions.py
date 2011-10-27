#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

arch = "i386" if get.ARCH() == "i686" else "x86_64"

WorkDir = "%s-%s-1100.%s.linux" % (get.srcNAME(), get.srcVERSION(), arch)

def install():
    shelltools.system("./install --prefix /usr --force --repackage %s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/browser-plugins/libflashplayer.so", "/usr/lib/opera/plugins/libflashplayer.so")
