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

def setup():
    # Remove source files
    shelltools.unlink("usbdux/*dux")
    shelltools.unlink("*/*.asm")

    # These + a lot of other firmware are shipped within alsa-firmware
    for fw in ("ess", "korg", "sb16", "yamaha"):
        shelltools.unlinkDir(fw)

    # This is already under v4l-dvb-firmware/
    shelltools.unlink("dvb-fe-xc5000-1.6.114.fw")

def install():
    pisitools.insinto("/lib/firmware", "*")

    # Remove installed WHENCE and LIC* files from /lib/firmware
    pisitools.remove("/lib/firmware/GPL-3")
    pisitools.remove("/lib/firmware/WHENCE*")
    pisitools.remove("/lib/firmware/LICENCE*")
    pisitools.remove("/lib/firmware/LICENSE*")

    # These firmwares are not needed in Pardus 2011 (2.6.36)
    pisitools.domove("/lib/firmware/nouveau-firmware-1/*", "/lib/firmware/nouveau")
    pisitools.removeDir("/lib/firmware/nouveau-firmware-1")

    # Install v4l-dvb-firmware's under /lib/firmware
    pisitools.domove("/lib/firmware/v4l-dvb-firmware/*.fw", "/lib/firmware")

    # Move wrong file under RTL8192SU
    pisitools.domove("/lib/firmware/RTL8192SE/rtl8192sfw.bin", "/lib/firmware/RTL8192SU/")

    # Install LICENSE files
    pisitools.dodoc("WHENCE", "LICENCE.*", "LICENSE.*", "GPL-3")
    pisitools.dodoc("v4l-dvb-firmware/BOM", "v4l-dvb-firmware/LICEN*")

    pisitools.removeDir("/lib/firmware/v4l-dvb-firmware")
