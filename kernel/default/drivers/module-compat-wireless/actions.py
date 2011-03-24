#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()

def setup():
    # Dump code-metrics before building :)
    shelltools.system("cat code-metrics.txt")

    for f in ("config.mk", "scripts/gen-compat-autoconf.sh"):
        pisitools.dosed(f, "@KERNELRELEASE@", KDIR)

def build():
    autotools.make("KLIB=/lib/modules/%s" % KDIR)

def install():
    autotools.install("KLIB=/lib/modules/%s KMODPATH_ARG='INSTALL_MOD_PATH=%s' DEPMOD=/bin/true" % (KDIR, get.installDIR()))

    pisitools.dodoc("COPYRIGHT", "README")
