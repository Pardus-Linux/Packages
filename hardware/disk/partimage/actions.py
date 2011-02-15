#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("--docdir=%s/%s/%s \
                         --disable-static \
                         --enable-gui-qt \
                         --enable-gui-newt \
                         --enable-gui-text \
                         --enable-ssl \
                         --enable-nls \
                         --enable-pam" % (get.installDIR(), get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("BUGS", "AUTHORS", "ABOUT-NLS", "COPYING", "THANKS")
    pisitools.dodoc("ChangeLog", "FORMAT", "README", "README.partimaged")
