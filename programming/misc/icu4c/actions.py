#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="icu/source"

def setup():
    autotools.autoconf("-f")
    autotools.configure("--with-data-packaging=library --disable-samples")
    pisitools.dosed("config/mh-linux", "-nodefaultlibs -nostdlib")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.move("%s/usr/sbin/*" % get.installDIR(),"%s/usr/bin" % get.installDIR())
    pisitools.removeDir("/usr/sbin")
