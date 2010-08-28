#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # Fix underlinking problem in python bindings
    pisitools.dosed("bindings/python/Makefile.am", "^_gpod_la_LDFLAGS = (.*)$", "_gpod_la_LDFLAGS = `python-config --libs` \\1")

    autotools.autoreconf("-fi")
    libtools.libtoolize("--copy --force")
    autotools.automake()
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --with-python=/usr/bin/python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #remove docs
    pisitools.removeDir("/usr/share/gtk-doc")
