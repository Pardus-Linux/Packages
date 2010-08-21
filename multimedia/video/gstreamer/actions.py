#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    #shelltools.system("./autogen.sh --disable-gtk-doc --disable-docbook")

    autotools.configure('--with-package-name="GStreamer package for Pardus" \
                         --with-package-origin="http://www.pardus.org.tr/eng" \
                         --enable-tests \
                         --enable-nls \
                         --disable-dependency-tracking \
                         --disable-examples \
                         --disable-failing-tests \
                         --disable-static \
                         --disable-rpath \
                         --disable-valgrind \
                         --disable-gtk-doc')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
