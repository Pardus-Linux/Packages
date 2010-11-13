#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ecore-1.0.0.beta2"

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-glib \
                         --enable-ecore-evas \
                         --enable-ecore-con \
                         --enable-ecore-ipc \
                         --enable-ecore-file \
                         --enable-ecore-input \
                         --enable-ecore-imf \
                         --enable-ecore-x \
                         --enable-ecore-fb \
                         --enable-ecore-directfb \
                         --enable-ecore-evas-fb \
                         --enable-ecore-evas-directfb \
                         --enable-ecore-evas-software-buffer \
                         --enable-ecore-evas-software-x11 \
                         --enable-ecore-evas-xrender-x11 \
                         --enable-ecore-evas-opengl-x11 \
                         --enable-openssl \
                         --enable-inotify \
                         --enable-poll \
                         --enable-curl \
                         --disable-gnutls \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
