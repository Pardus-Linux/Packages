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
    shelltools.export("ac_cv_libsigsegv", "no")
    shelltools.export("AUTOPOINT", "true")
    autotools.configure("--with-libsigsegv-prefix=no")

def build():
    autotools.make()

def check():
    autotools.make("-j1 check diffout")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned binaries
    pisitools.remove("/usr/bin/*-%s" % get.srcVERSION())

    pisitools.dosym("gawk.1", "/usr/share/man/man1/awk.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LIMITATIONS", "NEWS", "PROBLEMS", "README")
