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
    autotools.configure("--enable-aa \
                         --enable-a52 \
                         --enable-alsa \
                         --enable-dvb \
                         --enable-dvbpsi \
                         --enable-dc1394 \
                         --enable-dca \
                         --enable-dv \
                         --enable-dvdnav \
                         --enable-dvdread \
                         --enable-faad \
                         --enable-flac \
                         --enable-freetype \
                         --enable-fribidi \
                         --enable-glx \
                         --enable-gnutls \
                         --enable-id3tag \
                         --enable-libcddb \
                         --enable-libmpeg2 \
                         --enable-libxml2 \
                         --enable-lirc \
                         --enable-live555 \
                         --enable-loader \
                         --enable-lua \
                         --enable-mad \
                         --enable-mkv \
                         --enable-mod \
                         --enable-mozilla \
                         --enable-mpc \
                         --enable-ogg \
                         --enable-opengl \
                         --enable-png \
                         --enable-projectm \
                         --enable-pulse \
                         --enable-qt4 \
                         --enable-realrtsp \
                         --enable-screen \
                         --enable-sdl \
                         --enable-shared \
                         --enable-skins2 \
                         --enable-smb \
                         --enable-sout \
                         --enable-speex \
                         --enable-svg \
                         --enable-theora \
                         --enable-twolame \
                         --enable-upnp \
                         --enable-v4l \
                         --enable-vcd \
                         --enable-vcdx \
                         --enable-vlm \
                         --enable-vorbis \
                         --enable-x264 \
                         --enable-xvideo \
                         --disable-altivec \
                         --disable-bonjour \
                         --disable-gnomevfs \
                         --disable-growl \
                         --disable-jack \
                         --disable-portaudio \
                         --disable-snapshot \
                         --disable-static \
                         --with-mozilla-pkg=libxul \
                         --with-x %s " % dllloader )


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

