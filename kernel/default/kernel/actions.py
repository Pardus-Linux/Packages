#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linux-2.6.35"
NoStrip = ["/"]

perf_make = "-C tools/perf V=1 NO_DEMANGLE=1 NO_NEWT=1 prefix=/%s" % get.defaultprefixDIR()

def setup():
    # FIXME: This may be hidden in kerneltools.configure
    shelltools.copy("configs/kernel-%s-config" % get.ARCH(), ".config")
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)

    # Build perf
    #autotools.make("%s all" % perf_make)

def install():
    kerneltools.install()

    # Dump kernel version into /etc/kernel/
    kerneltools.dumpVersion()

    # Install kernel headers needed for out-of-tree module compilation
    # You can provide a list of extra directories from which to grab *.h files.
    kerneltools.installHeaders(extra=["drivers/media/dvb/dvb-core",
                                      "drivers/media/dvb/frontends",
                                      "drivers/media/video"])

    kerneltools.installLibcHeaders()

    # Install kernel source
    kerneltools.installSource()

    # Clean module-init-tools related stuff
    kerneltools.cleanModuleFiles()

    # FIXME: Provide perf wrapper
    #pisitools.insinto("/usr/bin", "tools/perf/perf", "perf.%s-%s" % (get.srcNAME(), get.srcVERSION()))
    #autotools.rawInstall("%s DESTDIR=%s install" % (perf_make, get.installDIR()))
