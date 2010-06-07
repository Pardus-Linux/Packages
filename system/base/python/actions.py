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

def setup():
    shelltools.export("OPT", "%s -fPIC" % get.CFLAGS())

    # Uncomment to use installed libffi as does other distributions and replace 
    # shelltools.export("CPPFLAGS", "%s" % os.popen("pkg-config --cflags-only-I libffi").read().strip())
    # shelltools.system("rm -rf Modules/_ctypes/libffi*")

    autotools.autoreconf()
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions \
                         --without-system-ffi")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    pisitools.dosym("/usr/bin/python2.6","/usr/bin/python")
    pisitools.dosym("/usr/bin/python2.6-config","/usr/bin/python-config")
    pisitools.dosym("/usr/lib/python2.6/pdb.py","/usr/bin/pdb")

    pisitools.remove("/usr/bin/idle")
    pisitools.remove("/usr/bin/pydoc")
    pisitools.remove("/usr/bin/smtpd.py")
    pisitools.remove("/usr/bin/2to3")
    pisitools.removeDir("/usr/lib/python2.6/idlelib")

    tkinterFile = "/usr/lib/python2.6/lib-dynload/_tkinter.so"
    if shelltools.isFile("%s/%s" % (get.installDIR(), tkinterFile)):
        pisitools.remove(tkinterFile)
        pisitools.removeDir("/usr/lib/python2.6/lib-tk")

    pisitools.dodoc("LICENSE", "README")
