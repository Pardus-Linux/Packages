# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    for d in ("etc", "usr"):
        pisitools.insinto("/", d)

    # Remove these when KDE is ready for 2011
    for config in ("kdeglobals", "kickoffrc", "ksplashrc"):
        pisitools.remove("/usr/share/kde4/config/%s" % config)
