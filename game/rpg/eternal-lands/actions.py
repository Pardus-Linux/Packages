#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ='elc-%s' % get.srcVERSION()

datadir = "/usr/share/eternal-lands"

def setup():
    pisitools.dosed("Makefile.linux", "-O0 -ggdb", "%s -DUSE_ACTOR_DEFAULTS" % get.CFLAGS())

def build():
    autotools.make("-f Makefile.linux")

def install():
    pisitools.dobin("el.x86.linux.bin")
    pisitools.rename("/usr/bin/el.x86.linux.bin", "eternal-lands")

    # These files conflicts with the ones found in eternal-lands-date package
    #pisitools.insinto(datadir, "*.xml")

    pisitools.insinto(datadir, "*.ini")

    pisitools.dohtml("docs/eye_candy/*")
    pisitools.dodoc("CHANGES", "TODO", "*.txt")
