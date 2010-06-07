#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="man-db-%s" % get.srcVERSION()

def setup():
     autotools.configure("--disable-setuid \
                          --disable-rpath \
                          --docdir=/%s/%s \
                          --with-device=utf8 \
                          --with-gnu-ld \
                          --with-config-file=/etc/man.conf \
                          --with-db=gdbm \
                          --enable-mb-groff \
                          --enable-nls \
                          --without-included-gettext" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make("nls=all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")
