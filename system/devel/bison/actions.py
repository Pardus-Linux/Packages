#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-nls")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/yacc")
    pisitools.remove("/usr/share/man/man1/yacc.1")
    pisitools.remove("/usr/share/bison/README")

    pisitools.removeDir("/usr/lib/")

    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README", "COPYING")
