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

arch = get.ARCH().replace("x86_64", "x86-64")

def setup():
    shelltools.export("CFLAGS", "-march=%s -O2 -pipe -fomit-frame-pointer" % arch)
    shelltools.export("CXXFLAGS", "-march=%s -O2 -pipe -fomit-frame-pointer" % arch)

    # FIXME: this may not be necessary for biarch
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")

    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system('../configure \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-gxx-include-dir=/usr/include/c++ \
                       --build=%s \
                       --disable-libgcj \
                       --disable-multilib \
                       --disable-nls \
                       --disable-mudflap \
                       --disable-libmudflap \
                       --enable-checking=release \
                       --enable-clocale=gnu \
                       --enable-__cxa_atexit \
                       --enable-languages=c,c++,fortran,objc \
                       --enable-libstdcxx-allocator=new \
                       --disable-libstdcxx-pch \
                       --enable-shared \
                       --enable-ssp \
                       --disable-libssp \
                       --enable-threads=posix \
                       --without-included-gettext \
                       --without-system-libunwind \
                       --with-system-zlib \
                       --with-tune=generic \
                       --with-pkgversion="Pardus Linux" \
                       --with-bugurl=http://bugs.pardus.org.tr' % get.HOST())
                       # FIXME: this is supposed to be detected automatically
                       #--enable-long-long \


def build():
    shelltools.export("CFLAGS", "-march=%s -O2 -pipe -fomit-frame-pointer" % arch)
    shelltools.export("CXXFLAGS", "-march=%s -O2 -pipe -fomit-frame-pointer" % arch)

    # FIXME: this may not be necessary for biarch
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")

    shelltools.cd("build")
    autotools.make('BOOT_CFLAGS="%s" profiledbootstrap' % get.CFLAGS())

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for header in ["limits.h","syslimits.h"]:
        pisitools.insinto("/usr/lib/gcc/%s/4.3.3/include" % get.HOST() , "gcc/include-fixed/%s" % header)

    # Not needed
    pisitools.removeDir("/usr/lib/gcc/*/*/include-fixed")
    pisitools.removeDir("/usr/lib/gcc/*/*/install-tools")

    # This one comes with binutils
    pisitools.remove("/usr/lib*/libiberty.a")

    # cc symlink
    pisitools.dosym("/usr/bin/gcc" , "/usr/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    pisitools.dosym("/usr/bin/cpp", "/lib/cpp")

