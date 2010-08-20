# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xf86-input-wacom-%s" % get.srcVERSION()

def setup():
    #shelltools.move("fdi/wacom.fdi", "11-x11-wacom.fdi")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.insinto("/usr/share/hal/fdi/policy/20thirdparty", "11-x11-wacom.fdi")

    pisitools.dodoc("AUTHORS", "ChangeLog", "GPL", "README")
