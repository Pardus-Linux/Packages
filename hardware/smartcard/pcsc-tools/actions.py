#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/usr" % get.installDIR())

    pisitools.remove("/usr/bin/gscriptor")
    pisitools.remove("/usr/share/man/man1/gscriptor.1p.gz")

    pisitools.dodoc("Changelog", "TODO", "README", "LICENCE")
