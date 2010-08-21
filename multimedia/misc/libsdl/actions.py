#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL-%s" % get.srcVERSION()
docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -O3" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fPIC -O3" % get.CXXFLAGS())

    # for libtool version matching
    shelltools.copy("/usr/share/aclocal/ltversion.m4", "acinclude/")
    shelltools.system("./autogen.sh")

    libtools.libtoolize("--force --copy")
    autotools.configure("--enable-events \
                         --enable-cpuinfo \
                         --enable-cdrom \
                         --enable-threads \
                         --enable-timers \
                         --enable-file \
                         --enable-alsa \
                         --enable-oss \
                         --enable-nasm \
                         --enable-video-aalib \
                         --enable-video-caca \
                         --enable-video-directfb \
                         --enable-video-fbcon \
                         --enable-video-dummy \
                         --enable-video-opengl \
                         --enable-video-x11 \
                         --enable-video-x11-xv \
                         --enable-video-x11-xinerama \
                         --enable-video-x11-xrandr \
                         --with-x \
                         --disable-rpath \
                         --disable-arts \
                         --disable-dga \
                         --disable-esd \
                         --disable-nas \
                         --disable-video-dga \
                         --disable-video-ggi \
                         --disable-video-svga \
                         --disable-video-x11-xme \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    libtools.preplib()

    for i in ["html", "images", "index.html"]:
        pisitools.insinto(docdir, "docs/%s" % i)

    pisitools.dodoc("BUGS", "CREDITS", "README", "README-SDL.txt", "README.CVS", "TODO", "WhatsNew")

