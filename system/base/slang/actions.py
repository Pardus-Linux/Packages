#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --with-png \
                         --with-readline=gnu")

def build():
    autotools.make("-j1 install_doc_dir=/%s/%s all" % (get.docDIR(), get.installDIR()))

def install():
    autotools.rawInstall("DESTDIR=%s INST_LIB_DIR=%s/usr/lib" % (get.installDIR(),get.installDIR()))
