#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cpupowerutils-cpupowerutils"

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s \
                          mandir=/%s \
                          docdir=/%s/%s" % (get.installDIR(), get.manDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("AUTHORS", "README", "COPYING")
