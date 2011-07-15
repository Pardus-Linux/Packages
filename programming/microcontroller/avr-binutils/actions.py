#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"

TOOLCHAIN_DIR="/opt/toolchain/avr"
_build_dir="build-avr"

def unset():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")

def setup():
    unset()

    shelltools.makedirs(_build_dir)
    shelltools.cd(_build_dir)
    shelltools.system("\
            ../configure \
            --mandir=/%s \
            --datadir=/%s \
            --prefix=%s \
            --target=avr \
            --disable-nls" % (get.manDIR(), get.dataDIR(), TOOLCHAIN_DIR))

def build():
    unset()

    shelltools.cd(_build_dir)
    autotools.make()

def install():
    shelltools.cd(_build_dir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove multiple binutils info files
    pisitools.removeDir("%s/share/" % TOOLCHAIN_DIR)

