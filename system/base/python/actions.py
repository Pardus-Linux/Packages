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

import os

WorkDir = "Python-%s" % get.srcVERSION()

PythonVersion = "2.7"

def setup():
    shelltools.export("OPT", "%s -fPIC -fwrapv" % get.CFLAGS())

    shelltools.unlinkDir("Modules/expat")
    #shelltools.unlinkDir("Modules/zlib")
    # Uncomment to use installed libffi as does other distributions and replace 
    shelltools.export("CPPFLAGS", "%s" % os.popen("pkg-config --cflags-only-I libffi").read().strip())
    shelltools.system("rm -rf Modules/_ctypes/libffi*")

    # Bump required autoconf version
    pisitools.dosed("configure.in", r"\(2.65\)", "(2.67)")

    autotools.autoreconf("-vif")
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions \
                         --with-system-expat \
                         --with-system-ffi")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    pisitools.dosym("/usr/bin/python%s" % PythonVersion, "/usr/bin/python")
    pisitools.dosym("/usr/bin/python%s-config" % PythonVersion, "/usr/bin/python-config")
    pisitools.dosym("/usr/lib/python%s/pdb.py" % PythonVersion, "/usr/bin/pdb")

    pisitools.dodoc("LICENSE", "README")
