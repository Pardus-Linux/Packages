#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # sanitize flags
    pisitools.dosed("configure", "-mno-ieee-fp")
    pisitools.dosed("configure", "-mfused-madd")
    pisitools.dosed("configure", "-mcpu=750")
    pisitools.dosed("configure", "-O20")

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc")

    pisitools.dodoc("AUTHORS", "README", "todo.txt", "doc/*.txt")
    pisitools.dohtml("doc/*")
