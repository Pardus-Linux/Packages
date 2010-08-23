#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", ""))

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-cplusplus \
                         --enable-large-config \
                         --enable-parallel-mark \
                         --enable-threads=posix \
                         --with-libatomic-ops=no")

def build():
    autotools.make()
    autotools.make("-C libatomic_ops")

def check():
    autotools.make("check")
    autotools.make("check -C libatomic_ops")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C libatomic_ops" % get.installDIR())

    pisitools.removeDir("/usr/share/gc")
    pisitools.removeDir("/usr/share/libatomic_ops")

    # Install libatomic_ops documentation
    pisitools.dodoc("libatomic_ops/doc/COPYING", "libatomic_ops/doc/*.txt", destDir="libatomic_ops")

    pisitools.dodoc("ChangeLog", "doc/README", "doc/README.linux")
