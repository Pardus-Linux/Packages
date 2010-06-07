#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.system("./setup.py install %s" % get.installDIR())

    pisitools.dodir("/etc/network")
    pisitools.dodir("/etc/mudur/services/enabled")
    pisitools.dodir("/etc/mudur/services/disabled")
    pisitools.dodir("/etc/mudur/services/conditional")
