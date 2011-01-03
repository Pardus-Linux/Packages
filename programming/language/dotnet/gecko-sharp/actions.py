#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007,2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gecko-sharp-2.0-%s" % get.srcVERSION()

def setup():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.configure()

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README*")
