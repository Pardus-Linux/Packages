#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    options = "--disable-static \
               --disable-sqlite \
               --enable-flac \
               --enable-alsa \
               --enable-largefile \
               --disable-gcc-pipe \
               --disable-jack \
               --disable-octave \
               --disable-gcc-werror \
               --disable-dependency-tracking"

    pisitools.dosed("examples/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")
    pisitools.dosed("tests/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")

    shelltools.unlink("M4/libtool.m4")

    for i in shelltools.ls("M4/lt*.m4"):
        shelltools.unlink(i)

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())

    autotools.autoreconf("-fi -I M4")
    autotools.configure(options)

    pisitools.dosed("doc/Makefile", "^htmldocdir.*", "htmldocdir = /usr/share/doc/%s/html" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
