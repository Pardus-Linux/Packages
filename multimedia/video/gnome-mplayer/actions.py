#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gnome-mplayer"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --with-gio \
                         --enable-nautilus=no \
                         --with-libgpod \
                         --with-libnotify \
                         --with-libmusicbrainz3 \
                         --without-gpm-new-method \
                         --without-gpm-old-method \
                         --disable-schemas-install")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # installing manually since make install causes sandbox violation
    pisitools.insinto("/etc/gconf/schemas/", "gnome-mplayer.schemas")

    pisitools.remove("/%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))
