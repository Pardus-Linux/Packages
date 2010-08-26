#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-ladcca \
                         --disable-lash \
                         --disable-dependency-tracking \
                         --disable-portaudio-support \
                         --disable-static \
                         --enable-jack-support \
                         --enable-alsa-support \
                         --enable-ladspa \
                         --enable-libsndfile-support")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO")
