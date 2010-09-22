#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/scripts/gcc.mak.in", "prefix=/usr/local", "prefix=/usr")

    # Bad workaround to make use of internal png header
    shelltools.copy("lib/libpng/pngpriv.h", "src/")

    #Ensure using system libraries
    shelltools.unlinkDir("lib/libpng")
    shelltools.unlinkDir("lib/zlib")

    autotools.rawConfigure("--with-system-zlib \
                         --with-system-libpng")

def build():
    autotools.make('-C src -f scripts/gcc.mak LDFLAGS="%s" CFLAGS="%s" CC="%s"' % (get.LDFLAGS(), get.CFLAGS(), get.CC()))

def install():
    pisitools.dobin("src/optipng")

    pisitools.doman("man/optipng.1")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("LICENSE.txt", "README.txt", "doc/caveat.txt", "doc/history.txt", "doc/todo.txt")
