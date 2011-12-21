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
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")

    # For being able to build as root, pff
    shelltools.export("FORCE_UNSAFE_CONFIGURE", "1")

    autotools.configure("--disable-rpath")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/sbin")

    # Drop rmt tool
    pisitools.removeDir("/usr/libexec")

    pisitools.doman("doc/tar.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "THANKS")
