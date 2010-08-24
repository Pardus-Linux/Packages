#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="gpac"

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    pisitools.dosed("configure", '^has_wx="yes', 'has_wx="no')
    shelltools.chmod("configure")
    autotools.configure('--enable-svg \
                         --enable-pic \
                         --disable-wx \
                         --disable-amr \
                         --use-a52=no \
                         --use-ffmpeg=no \
                         --use-ogg=system \
                         --use-vorbis=system \
                         --use-theora=system \
                         --use-faad=system \
                         --use-png=system \
                         --use-jpeg=system \
                         --use-ft=system \
                         --use-js=system \
                         --use-mad=system \
                         --cc="%s" \
                         --disable-oss-audio' % get.CC())

def build():
    autotools.make('-j1 OPTFLAGS="%s -fno-strict-aliasing"' % get.CFLAGS())

def install():
    autotools.rawInstall('STRIP="true" DESTDIR="%s"' % get.installDIR())
    autotools.rawInstall('STRIP="true" DESTDIR="%s"' % get.installDIR(), "install-lib")

    # No static libs
    pisitools.remove("/usr/lib/libgpac_static.a")

    pisitools.dosym("/usr/bin/MP4Box","/usr/bin/mp4box")
    pisitools.dosym("/usr/bin/MP4Client","/usr/bin/mp4client")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/*.txt")
    pisitools.doman("doc/man/*.1")

