#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-src" % get.srcDIR()
datadir = "/usr/share/teeworlds"
NoStrip = [datadir]

def setup():
    shelltools.cd("bam-0.2.0")
    shelltools.chmod("make_unix.sh", 0755)
    shelltools.system("./make_unix.sh")

def build():
    shelltools.system('CFLAGS="%s" ./bam-0.2.0/src/bam release' % get.CFLAGS())

def install():
    pisitools.dobin("teeworlds")
    pisitools.dobin("teeworlds_srv")
    pisitools.rename("/usr/bin/teeworlds_srv", "teeworlds-server")

    pisitools.insinto(datadir, "data/*")

    pisitools.dodoc("*.txt")
