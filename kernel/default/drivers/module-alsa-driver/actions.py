#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()
NoStrip = ["/"]

if "_" in get.srcVERSION():
    # Snapshot
    WorkDir = "alsa-driver"
else:
    # Upstream tarball
    WorkDir = "alsa-driver-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-oss \
                         --with-kernel=/lib/modules/%s/build \
                         --with-build=/lib/modules/%s/build \
                         --with-isapnp=yes \
                         --with-sequencer=yes \
                         --with-card-options=all \
                         --disable-verbose-printk \
                         --enable-dynamic-minors \
                         --with-cards=all" % (KDIR, KDIR))

    # Needed for V4L stuff
    shelltools.sym("%s/alsa-driver/include/config.h" % get.workDIR(), "%s/alsa-driver/sound/include/config.h" % get.workDIR())
    shelltools.sym("%s/alsa-driver/include/config1.h" % get.workDIR(), "%s/alsa-driver/sound/include/config1.h" % get.workDIR())

    # Configure hda-emu
    """
    shelltools.cd("hda-emu")
    autotools.autoreconf("-fi")
    autotools.configure("--with-hdadir=../alsa-kernel/pci/hda")
    """

def build():
    autotools.make()
    #autotools.make("-C hda-emu")

    # Build v4l drivers
    shelltools.copy("Module.symvers", "v4l/")
    autotools.make("-C /lib/modules/%s/build M=%s/v4l V=1 modules" % (KDIR, get.curDIR()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-modules")

    #autotools.rawInstall("DESTDIR=%s -C hda-emu" % get.installDIR())

    # FIXME: Install v4l drivers
    #for d in ["saa7134", "cx88", "cx231xx", "em28xx"]:
    #    pisitools.insinto("/lib/modules/%s/kernel/sound/drivers" % KDIR, "v4l/%s/*.ko" % d)

    # Copy symvers file for external module building like saa7134-alsa, cx2388-alsa, etc.
    #pisitools.insinto("/lib/modules/%s/kernel/sound" % KDIR, "Module.symvers", "Module.symvers.alsa")

    # Install headers
    pisitools.insinto("/usr/include/sound/", "alsa-kernel/include/*.h")

    # Install alsa-info
    pisitools.insinto("/usr/bin", "utils/alsa-info.sh", "alsa-info")

    for f in shelltools.ls("alsa-kernel/Documentation/*txt"):
        pisitools.dodoc(f)

    pisitools.dodoc("doc/serialmidi.txt")
