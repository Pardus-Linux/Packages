#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = "/"

TOOLCHAIN_DIR="/opt/toolchain/avr"
_build_dir="build-avr"

def fix_env():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")
    # Bash doesnt activate this path immediately after avr-binutils install
    shelltools.export("PATH", "%s:%s/bin" % (get.ENV("PATH"), TOOLCHAIN_DIR) )

def setup():
    fix_env()

    shelltools.makedirs(_build_dir)
    shelltools.cd(_build_dir)
    shelltools.system('\
            ../configure \
            --target=avr \
            --mandir=/%s \
            --datadir=/%s \
            --prefix=%s \
            --enable-languages="c,c++" \
            --disable-nls \
            --disable-libssp \
            --with-dwarf2 \
            --with-system-zlib \
            --enable-version-specific-runtime-libs \
            --with-pkgversion="Pardus Linux" \
            --with-bugurl=http://bugs.pardus.org.tr \
            ' % (get.manDIR(), get.dataDIR(), TOOLCHAIN_DIR))

def build():
    fix_env()

    shelltools.cd(_build_dir)
    autotools.make()

def install():
    fix_env()

    shelltools.cd(_build_dir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove unneccessary binutils files
    for d in ("%s/share/" % TOOLCHAIN_DIR,
              "%s/lib/gcc/avr/4.5.1/install-tools" % TOOLCHAIN_DIR,
              "%s/libexec/gcc/avr/4.5.1/install-tools" % TOOLCHAIN_DIR,
              "%s/include" % TOOLCHAIN_DIR,
              "/usr/share/man/man7"):
        pisitools.removeDir(d)

    pisitools.remove("%s/lib/libiberty.a" % TOOLCHAIN_DIR)

