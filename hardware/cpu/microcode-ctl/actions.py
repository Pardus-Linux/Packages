#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "microcode_ctl-%s" % get.srcVERSION()

amd_ucode = "amd-ucode-2009-10-09"

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))


def install():
    autotools.install("DESTDIR=%s PREFIX=/usr INSDIR=/sbin" % get.installDIR())

    # Install the intel one
    pisitools.insinto("/lib/firmware", "data/microcode-*", "microcode.dat")

    # Install the AMD one
    pisitools.insinto("/lib/firmware/amd-ucode", "data/%s/microcode_amd.bin" % amd_ucode)

    pisitools.newdoc("data/%s/README" % amd_ucode, "README.microcode_amd")
    pisitools.newdoc("data/%s/LICENSE" % amd_ucode, "LICENSE.microcode_amd")

    pisitools.dodoc("Changelog", "README")

