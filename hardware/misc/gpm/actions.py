#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    autotools.configure("--libdir=/usr/lib \
                         --sysconfdir=/etc/gpm")

def build():
    autotools.make("clean")
    autotools.make("-j1 -C doc")
    autotools.make("-j1 EMACS=:")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove this when we can break abi
    pisitools.dosym("libgpm.so.1", "/usr/lib/libgpm.so")

    #remove static link
    pisitools.remove("/usr/lib/libgpm.a")

    pisitools.insinto("/etc/gpm", "conf/gpm-*.conf")

    pisitools.dodoc("BUGS", "Changes", "README", "TODO", "doc/Announce", "doc/FAQ", "doc/README*")
