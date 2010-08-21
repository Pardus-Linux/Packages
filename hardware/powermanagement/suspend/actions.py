# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "suspend-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-static \
                         --enable-compress \
                         --disable-encrypt \
                         --with-initramfsdir=/usr/sbin")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/dev")

    # will be created by postInstall script
    pisitools.remove("/etc/suspend.conf")

    shelltools.touch("%s/etc/suspend.key" % get.installDIR())
