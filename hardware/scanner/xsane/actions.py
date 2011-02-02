#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("include/config.h")

    shelltools.makedirs("withgimp")
    shelltools.makedirs("withoutgimp")

    shelltools.cd("withgimp")
    shelltools.sym("../configure", "configure")

    autotools.configure("--enable-gimp")

    shelltools.cd("../withoutgimp")
    shelltools.sym("../configure", "configure")
    autotools.configure("--disable-gimp")

def build():
    autotools.make("-C withgimp")
    autotools.make("-C withoutgimp")

def install():
    autotools.rawInstall("-C withoutgimp DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins", "withgimp/src/xsane")

    pisitools.dodoc("xsane.*")
    pisitools.remove("/usr/share/doc/xsane/xsane.spe*")
    pisitools.remove("/usr/share/doc/xsane/xsane.RPM")

    pisitools.removeDir("/usr/sbin")
