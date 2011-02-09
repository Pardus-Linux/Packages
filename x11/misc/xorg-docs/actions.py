#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

x11docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-txt \
                         --enable-pdf \
                         --disable-ps \
                         --disable-html \
                         --with-x11docdir=%s" % x11docdir)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
