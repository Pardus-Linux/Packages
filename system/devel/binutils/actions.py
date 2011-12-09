#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

multilib = "--enable-multilib" if get.ARCH() == "x86_64" else ""

def setup():
    # Build binutils with LD_SYMBOLIC_FUNCTIONS=1 and reduce PLT relocations in libfd.so by 84%.
    shelltools.export("LD_SYMBOLIC_FUNCTIONS", "1")

    autotools.configure('--enable-shared \
                         --host=%s \
                         --target=%s \
                         --enable-gold \
                         --enable-plugins \
                         --enable-threads \
                         --with-pkgversion="Pardus Linux" \
                         --with-bugurl=http://bugs.pardus.org.tr/ \
                         --with-separate-debug-dir=/usr/lib/debug \
                         %s \
                         --disable-nls \
                         --disable-werror' % (get.HOST(), get.HOST(), multilib))
                         # --with-pic \
                         # --enable-targets="i386-linux" \

def build():
    autotools.make("tooldir=/usr all")
    autotools.make("tooldir=/usr info")

# check fails because of LD_LIBRARY_PATH
#def check():
#    autotools.make("check -j1")

def install():
    autotools.rawInstall("DESTDIR=%s tooldir=/usr" % get.installDIR())

    # Copy plugin-api.h file to build LLVM with LLVM gold plugin
    pisitools.insinto("/usr/include", "include/plugin-api.h")

    # Rebuild libiberty with -fPIC
    autotools.make("-C libiberty clean")
    autotools.make('CFLAGS="-fPIC %s" -C libiberty' % get.CFLAGS())

    # Rebuild libbfd with -fPIC
    autotools.make("-C bfd clean")
    autotools.make('CFLAGS="-fPIC %s" -C bfd' % get.CFLAGS())

    # Rebuild libopcodes with -fPIC
    autotools.make("-C opcodes clean")
    autotools.make('CFLAGS="-fPIC %s" -C opcodes' % get.CFLAGS())


    # Install rebuilt static libraries
    pisitools.dolib_a("bfd/libbfd.a")
    pisitools.dolib_a("libiberty/libiberty.a")
    pisitools.dolib_a("opcodes/libopcodes.a")

    # Install header for libiberty
    pisitools.insinto("/usr/include", "include/libiberty.h")

    # Prevent programs to link against libbfd and libopcodes dynamically,
    # they are changing far too often
    pisitools.remove("/usr/lib/libopcodes.so")
    pisitools.remove("/usr/lib/libbfd.so")

    # Remove Windows/Novell specific man pages
    pisitools.remove("/usr/share/man/man1/dlltool.1")
    pisitools.remove("/usr/share/man/man1/nlmconv.1")
    pisitools.remove("/usr/share/man/man1/windres.1")


