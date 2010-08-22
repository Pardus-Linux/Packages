#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="aspell-sv-%s-0" % get.srcVERSION().replace(".0", "")

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/*", "COPYING", "Copyright", "info")
