#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ffmpeg"
version = "26223"
minimumcpu = "" if get.ARCH() == "x86_64" else "--cpu=atom"


def setup():
    # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=11203
    shelltools.export("CFLAGS","%s -DRUNTIME_CPUDETECT -O3 -fomit-frame-pointer -fPIC" % get.CFLAGS())
    pisitools.dosed("configure", "die_li.*aac")

    # to keep the source tarball small and to prevent sandbox problem of subversion, write svn version by hand
    shelltools.unlink("version.sh")
    shelltools.echo("version.sh", '#!/bin/bash\necho "#define FFMPEG_VERSION  \\\"SVN-r%s\\\"" > version.h' % version)
    shelltools.chmod("version.sh", 0755)

    # CPU thing is just used for CMOV detection
    autotools.rawConfigure("--prefix=/usr \
                            %s \
                            --mandir=/usr/share/man \
                            --enable-runtime-cpudetect \
                            --enable-gpl \
                            --enable-version3 \
                            --enable-pthreads \
                            --enable-postproc \
                            --enable-lsp \
                            --enable-x11grab \
                            --enable-libdc1394 \
                            --enable-libfaac \
                            --enable-libfreetype \
                            --enable-libgsm \
                            --enable-libmp3lame \
                            --enable-libnut \
                            --enable-libopencore-amrnb \
                            --enable-libopencore-amrwb \
                            --enable-libschroedinger \
                            --enable-libspeex \
                            --enable-libtheora \
                            --enable-libvorbis \
                            --enable-libvpx \
                            --enable-libx264 \
                            --enable-libxvid \
                            --enable-shared \
                            --enable-mmx \
                            --enable-mmx2 \
                            --enable-sse \
                            --enable-vaapi \
                            --enable-vdpau \
                            --enable-yasm \
                            --disable-stripping \
                            --disable-static \
                            --disable-debug" % minimumcpu)

                            # Not yet
                            # --enable-avfilter \
                            # --enable-avfilter-lavf \
                            # FIXME: this may be nice, or not
                            # --enable-hardcoded-tables \
                            # --disable-optimizations \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc","doc/ffserver.conf")

    pisitools.dodoc("Changelog", "README")
