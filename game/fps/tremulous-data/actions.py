#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "tremulous"
datadir = "/usr/share/tremulous"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("base/server.cfg", "set sv_hostname.*", 'set sv_hostname "Tremulous Server on Pardus"')
    fixperms("base")

def install():
    pisitools.dodir(datadir)
    shelltools.copytree("base", "%s/%s/" % (get.installDIR(), datadir))

    for f in ["CC", "ChangeLog", "COPYING", "GPL", "manual.pdf"]:
        pisitools.dodoc(f)

