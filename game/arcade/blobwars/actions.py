#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

params = {"datadir": get.dataDIR(), \
          "docdir": get.docDIR(), \
          "srctag": get.srcNAME(), \
          "installdir": get.installDIR()}

def build():
    autotools.make('DATADIR=/%(datadir)s/blobwars/ DOCDIR=/%(docdir)s/%(srctag)s/' % params)

def install():
    autotools.rawInstall('DESTDIR=%(installdir)s \
                          BINDIR=%(installdir)s/usr/bin/ \
                          DATADIR=%(installdir)s/%(datadir)s/blobwars/ \
                          DOCDIR=%(installdir)s/%(docdir)s/%(srctag)s/' % params)
