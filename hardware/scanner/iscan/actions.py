#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def setup():
    shelltools.unlink("m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --enable-frontend \
                         --enable-gimp=no \
                         --disable-rpath \
                         --disable-ltdl-install")

def build():
    autotools.make("-j1")

    shelltools.cd("po")
    autotools.make("update-po")

def install():
    autotools.install()

    # Install sane backend configuration file
    pisitools.insinto("/etc/sane.d", "backend/epkowa.conf")

    # Install documentation
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

