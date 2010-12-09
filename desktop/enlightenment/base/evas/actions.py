#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "evas-1.0.0.beta3"

def setup():
    autotools.autoreconf("-vfi")

    # async/pipe rendering is disabled due to bugs shown in x86 and arm.
    # Upstream is aware and has recommended to not to enable them.
    # http://trac.enlightenment.org/e/changeset/51691/trunk/evas/README.in
    autotools.configure("--enable-gl-x11 \
                         --enable-software-xlib \
                         --enable-xrender-x11 \
                         --enable-fb \
                         --enable-directfb \
                         --enable-async-events \
                         --enable-async-preload \
                         --disable-pipe-render \
                         --disable-async-render \
                         --enable-fribidi \
                         --enable-buffer \
                         --enable-pthreads \
                         --with-x \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
