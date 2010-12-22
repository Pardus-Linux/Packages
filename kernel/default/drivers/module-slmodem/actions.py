#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

WorkDir="slmodem-%s" % get.srcVERSION().replace("_", "-")
KDIR = kerneltools.getKernelVersion()

def setup():
    shelltools.export("CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))

    pisitools.dosed("drivers/Makefile", "SUBDIRS=\$(shell pwd)", "SUBDIRS=%s/drivers" % get.srcDIR())
    pisitools.dosed("drivers/Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("drivers/Makefile", "\$\(shell uname -r\)", KDIR)
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", KDIR)

def build():
    autotools.make("SUPPORT_ALSA=1 modem")
    autotools.make("KERNEL_DIR=/lib/modules/%s/build drivers" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "drivers/*.ko")
    pisitools.insinto("/usr/sbin", "modem/modem_test", "slmodem_test")
    pisitools.dosbin("modem/slmodemd")
    pisitools.dodir("/var/lib/slmodem")

    pisitools.dodoc("Changes", "README")

