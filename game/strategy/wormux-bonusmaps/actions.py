#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/wormux/map", "*")

    # These are now in the main Wormux distribution
    pisitools.removeDir("/usr/share/wormux/map/cowland")
    pisitools.removeDir("/usr/share/wormux/map/grenouilles")

    pisitools.remove("/usr/share/wormux/map/README")
    pisitools.remove("/usr/share/wormux/map/pisiBuildState")
