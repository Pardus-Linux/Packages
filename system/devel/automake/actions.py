#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

ver = "1.11"

def setup():
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use gnuconfig files
    for config in ["config.guess","config.sub"]:
        pisitools.remove("/usr/share/automake-%s/%s" % (ver, config))
        pisitools.dosym("/usr/share/gnuconfig/%s" % config, "/usr/share/automake-%s/%s" % (ver, config))

    pisitools.dodoc("NEWS", "README", "THANKS", "TODO", "AUTHORS", "ChangeLog*")
