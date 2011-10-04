# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

ARCH = "i386" if get.ARCH() == "i686" else "x86_64"
WorkDir = get.ARCH()
NoStrip = "/"

def install():
    distdir = "%s-%s-%s" % (get.srcNAME(), get.srcVERSION(), ARCH)

    shelltools.copytree("%s/usr" % distdir, "%s/usr" % get.installDIR())
    pisitools.doexe("%s/libflashplayer.so" % distdir, "/usr/lib/browser-plugins")
