#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    autotools.configure("--with-pcm-plugins=all \
                         --with-ctl-plugins=all \
                         --disable-dependency-tracking \
                         --with-versioned \
                         --with-libdl \
                         --with-pthread \
                         --with-librt \
                         --enable-shared \
                         --disable-static \
                         --disable-aload \
                         --enable-python")

    # rpath fix
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "TODO", "COPYING", "doc/*.txt")
