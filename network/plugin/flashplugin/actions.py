# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = get.ARCH()
NoStrip = "/"

def install():
    shelltools.copytree("usr", "%s/usr" % get.installDIR())

    pisitools.doexe("libflashplayer.so", "/usr/lib/browser-plugins")
