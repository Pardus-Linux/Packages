#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "iwlwifi-4965-ucode-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/lib/firmware", "*.ucode")
    shelltools.chmod("%s/lib/firmware/*.ucode" % get.installDIR(), 0644)
