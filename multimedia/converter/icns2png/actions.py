#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="libicns-%s"%get.srcVERSION()
def setup():
    autotools.configure()

def build():
    shelltools.export("CC", get.CC())
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" prefix="/usr"' % get.installDIR())
    pisitools.dodoc("README", "AUTHORS")
