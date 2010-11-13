#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "eina-1.0.0.beta2"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static\
                         --disable-magic-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
