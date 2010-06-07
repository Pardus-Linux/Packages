#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "busybox-%s" % get.srcVERSION()

def build():
    autotools.make()
    autotools.make("busybox.links")

def install():
    pisitools.insinto("/lib/initramfs", "busybox.links")
    pisitools.insinto("/lib/initramfs", "busybox")

    pisitools.dodir("/etc/initramfs.d")

