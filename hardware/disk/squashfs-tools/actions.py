#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s_%s" % (get.srcNAME(), get.srcVERSION())

def build():
    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    autotools.install("INSTALL_DIR='%s/usr/sbin'" % get.installDIR())
