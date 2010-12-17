#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

print "----"
WorkDir = "gfan0.4plus"
print "WorkDir:%s" % WorkDir

def build():
    autotools.make()

def install():
    autotools.rawInstall("BINDIR=%s/usr/bin" % get.installDIR())

    pisitools.dodoc("doc/*","COPYING", "README", "LICENSE")
