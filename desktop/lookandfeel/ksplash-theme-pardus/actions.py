#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

WorkDir = "./"

def install():
    pisitools.insinto("%s/ksplash/Themes/" % kde4.appsdir, "ksplash-pardus-theme", "Pardus")
    pisitools.insinto("%s/ksplash/Themes/" % kde4.appsdir, "ksplash-pardus-theme-milky", "Pardus-Milky")

