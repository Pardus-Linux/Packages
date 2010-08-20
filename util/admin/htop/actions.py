# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-taskstats \
                         --enable-unicode")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove empty dirs
    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/lib")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
