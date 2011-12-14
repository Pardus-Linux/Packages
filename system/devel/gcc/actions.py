#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

verMajor = get.srcVERSION()
arch = get.ARCH().replace("x86_64", "x86-64")

# WARNING: even -fomit-frame-pointer may break the build, stack protector, fortify source etc. are off limits
cflags = "-O2"

def removePardusSection(_dir):
    for root, dirs, files in os.walk(_dir):
        for name in files:
            # FIXME: should we do this only on nonshared or all ?
            # if ("crt" in name and name.endswith(".o")) or name.endswith("nonshared.a"):
            if ("crt" in name and name.endswith(".o")) or name.endswith(".a"):
                i = os.path.join(root, name)
                shelltools.system('objcopy -R ".comment.PARDUS.OPTs" -R ".note.gnu.build-id" %s' % i)

def exportFlags():
    # we set real flags with new configure settings, these are just safe optimizations
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cflags)

    # FIXME: this may not be necessary for biarch
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    shelltools.export("LC_ALL", "en_US.UTF-8")

def setup():
    exportFlags()
    # Maintainer mode off, do not force recreation of generated files
    # shelltools.system("contrib/gcc_update --touch")

    # Do not install libiberty
    # This one comes with binutils
    pisitools.dosed("libiberty/Makefile.in", "install_to_\$\(INSTALL_DEST\) ", "")

    # Do not run fixincludes
    pisitools.dosed("gcc/Makefile.in", "\./fixinc\.sh", "-c true")

    shelltools.makedirs("build")
    shelltools.cd("build")

    # multilib is disabled
    shelltools.system('../configure \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --build=%s \
                       --with-gxx-include-dir=/usr/include/c++ \
                       --enable-linker-build-id \
                       --enable-ssp \
                       --enable-clocale=gnu \
                       --enable-libstdcxx-allocator=new \
                       --enable-shared \
                       --enable-threads=posix \
                       --enable-checking=release \
                       --enable-multilib \
                       --disable-multilib \
                       --enable-bootstrap \
                       --with-system-zlib \
                       --with-system-libunwind \
                       --enable-__cxa_atexit \
                       --enable-gnu-unique-object \
                       --enable-languages=c,c++,fortran,objc,obj-c++,lto \
                       --enable-plugin \
                       --disable-nls \
                       --disable-libgcj \
                       --disable-libunwind-exceptions \
                       --disable-libstdcxx-pch \
                       --without-included-gettext \
                       --with-arch_32=i686 \
                       --with-tune=generic \
                       --with-pkgversion="Pardus Linux" \
                       --with-bugurl=http://bugs.pardus.org.tr' % get.HOST())

def build():
    exportFlags()

    shelltools.cd("build")
    autotools.make('BOOT_CFLAGS="%s" profiledbootstrap' % cflags)

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for header in ["limits.h","syslimits.h"]:
        pisitools.insinto("/usr/lib/gcc/%s/%s/include" % (get.HOST(), verMajor) , "gcc/include-fixed/%s" % header)

    # Not needed
    pisitools.removeDir("/usr/lib/gcc/*/*/include-fixed")
    pisitools.removeDir("/usr/lib/gcc/*/*/install-tools")

    # cc symlink
    pisitools.dosym("/usr/bin/gcc" , "/usr/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    pisitools.dosym("/usr/bin/cpp", "/lib/cpp")

    # Remove our options section from crt stuff
    """
    removePardusSection("%s/usr/lib/" % get.installDIR())
    if get.ARCH() == "x86_64":
        removePardusSection("%s/usr/lib32/" % get.installDIR())
    """

    # autoload gdb pretty printers
    gdbpy_dir = "/usr/share/gdb/auto-load/usr/lib/"
    pisitools.dodir(gdbpy_dir)

    gdbpy_files = shelltools.ls("%s/usr/lib/libstdc++*gdb.py*" % get.installDIR())
    for i in gdbpy_files:
        pisitools.domove("/usr/lib/%s" % shelltools.baseName(i), gdbpy_dir)

    #if arch == "x86-64":
    #    pisitools.remove("/usr/lib32/libstdc++*gdb.py*")

