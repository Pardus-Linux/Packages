#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "apmd-%s.orig" % get.srcVERSION().split("_")[0]

flags = "CC=%s CFLAGS='%s' LDFLAGS='%s'" % (get.CC(), get.CFLAGS(), get.LDFLAGS())

def setup():
    pisitools.dosed("Makefile", "-I/usr/src/linux/include")

def build():
    autotools.make(flags)

def install():
    autotools.rawInstall("%s DESTDIR=\"%s\" PREFIX=/usr LIBDIR=/usr/lib" % (flags, get.installDIR()))

    pisitools.doexe("debian/apmd_proxy", "/etc/apm")

    pisitools.dodir("/etc/apm/event.d")
    pisitools.dodir("/etc/apm/suspend.d")
    pisitools.dodir("/etc/apm/resume.d")
    pisitools.dodir("/etc/apm/other.d")
    pisitools.dodir("/etc/apm/scripts.d")

    # we already have one from pm-utils
    pisitools.remove("/usr/bin/on_ac_power")

    # We do not need apm library
    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/lib")

    pisitools.dodoc("AUTHORS", "apmsleep.README", "README", "debian/README.Debian", "debian/changelog*", "debian/copyright*")
    pisitools.doman("apm*.1", "apm*.8")
