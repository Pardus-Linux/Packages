#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--enable-shared \
                         --disable-dependency-tracking")

    shelltools.chmod("examples/*", 0644)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "doc/LZO*")

    pisitools.insinto(examples, "examples/*.c")
    pisitools.insinto(examples, "examples/*.h")
    pisitools.insinto(examples, "examples/Makefile.am")
