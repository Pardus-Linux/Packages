#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fvi")
    #autotools.autoconf("-f")
    autotools.configure("--disable-static \
                         --disable-introspection \
                         --disable-gtk-doc-html \
                         --disable-tests")

def build():
    autotools.make()

"""
#Requires dbus-test-runner (https://launchpad.net/dbus-test-runner)

def check():
    autotools.make("check")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README", "NEWS")

    pisitools.removeDir("/usr/share/gtk-doc")
