#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip=["/usr/share/kvm"]
WorkDir="kvm-kmod-%s" % get.srcVERSION().replace("_", "-")

def setup():
    # Fix PREFIX
    pisitools.dosed("Makefile", "^PREFIX =.*$", "PREFIX = /usr")
    pisitools.dosed("Makefile", "etc\/udev", "lib\/udev")

    # GROUP conversion here (kvm->virt)
    pisitools.dosed("scripts/65-kvm.rules", "GROUP=\"kvm\"", "GROUP=\"virt\"")

    autotools.rawConfigure("--kerneldir=/lib/modules/%s/build" % kerneltools.getKernelVersion())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
