#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.ARCH()

def install():
    pisitools.dodir("/opt")
    pisitools.insinto("/opt", "eclipse")

    # Make eclipse icon visible on start menu
    pisitools.insinto("/usr/share/pixmaps", "%s/opt/eclipse/plugins/org.eclipse.platform_3.6.2.v201102101200/eclipse48.png" % get.installDIR(), "eclipse.png")
