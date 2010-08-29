#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    cmaketools.configure("-DPHYSFS_BUILD_STATIC=OFF \
                          -DPHYSFS_BUILD_SHARED=ON \
                          -DPHYSFS_ARCHIVE_7Z=OFF \
                          -DPHYSFS_BUILD_TEST=OFF \
                          -DPHYSFS_BUILD_WX_TEST=OFF \
                          -DPHYSFS_INTERNAL_ZLIB=OFF \
                          ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("CHANGELOG.txt", "CREDITS.txt", "TODO.txt")
