#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

# enable loader builds DLL loader for ELF i386 platforms only
dllloader = "--disable-loader " if get.ARCH() == "x86_64" else ""

def setup():
    # Make it build with libtool 1.5
    shelltools.system("rm -rf m4/lt* m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --enable-qt4 \
                         --enable-vlm \
                         --enable-lua \
                         --enable-sout \
                         --enable-live555 \
                         --enable-realrtsp \
                         --enable-dvdread \
                         --enable-dvdnav \
                         --enable-smb \
                         --enable-dvbpsi \
                         --enable-v4l \
                         --enable-libcddb \
                         --enable-vcdx \
                         --enable-vcd \
                         --enable-dvb \
                         --enable-screen \
                         --enable-ogg \
                         --enable-mkv \
                         --enable-mpc \
                         --enable-mod \
                         --enable-mad \
                         --enable-twolame \
                         --enable-a52 \
                         --enable-dca \
                         --enable-flac \
                         --enable-libmpeg2 \
                         --enable-vorbis \
                         --enable-speex \
                         --enable-theora \
                         --enable-png \
                         --enable-faad \
                         --enable-aa \
                         --enable-loader \
                         --enable-xvideo \
                         --enable-glx \
                         --enable-opengl \
                         --enable-sdl \
                         --enable-freetype \
                         --enable-fribidi \
                         --enable-libxml2 \
                         --enable-svg \
                         --enable-skins2 \
                         --enable-alsa \
                         --enable-pulse \
                         --enable-lirc \
                         --enable-gnutls \
                         --enable-mozilla \
                         --with-mozilla-pkg=libxul \
                         --enable-x264 \
                         --enable-upnp \
                         --enable-id3tag \
                         --enable-projectm \
                         --with-x \
                         --disable-static \
                         --disable-altivec \
                         --disable-snapshot \
                         --disable-gnomevfs \
                         --disable-bonjour \
                         --disable-jack \
                         --disable-growl \
                         --disable-portaudio %s " % dllloader )

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/icons/%s/vlc*.png" % icon)

    # Fix Firefox plugin location
    pisitools.domove("/usr/lib/mozilla/plugins/*", "/usr/lib/browser-plugins")
    pisitools.remove("/usr/lib/browser-plugins/*.la")
    pisitools.removeDir("/usr/lib/mozilla/")

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "HACKING", "doc/fortunes.txt", "doc/intf-vcd.txt")

