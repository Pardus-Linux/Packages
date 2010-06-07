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

def setup():
    # Use secure delete. Even if the data is deleted with sqlite query, the traces of the deleted data still remains in the file
    # but cannot be seen with sqlite query. However, it can be seen by opening the file with a text editor.
    # SQLITE_SECURE_DELETE overwrites written data with zeros.
    shelltools.export("CFLAGS", "%s \
                       -DSQLITE_SECURE_DELETE=1 \
                       -DSQLITE_ENABLE_COLUMN_METADATA=1 \
                       -DSQLITE_DISABLE_DIRSYNC=1 \
                       -DSQLITE_ENABLE_FTS3=3 \
                       -DSQLITE_ENABLE_RTREE=1 \
                       -O3 -DNDEBUG=1 -fno-strict-aliasing" % get.CFLAGS())

    autotools.configure("--disable-static \
                         --enable-readline \
                         --enable-threadsafe")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
