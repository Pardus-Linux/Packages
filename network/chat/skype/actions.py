#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
NoStrip = ["/"]

def install():
    for data in ["avatars","lang","sounds"]:
        pisitools.insinto("/usr/share/skype",data)

    pisitools.dobin("skype")
    pisitools.rename("/usr/bin/skype", "skype.bin")

    # Dbus config
    pisitools.insinto("/etc/dbus-1/system.d", "skype.conf")

    pisitools.insinto("/usr/share/icons/hicolor/16x16/apps", "icons/SkypeBlue_16x16.png", "skype.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps", "icons/SkypeBlue_32x32.png", "skype.png")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "icons/SkypeBlue_48x48.png", "skype.png")

    pisitools.dodoc("README", "LICENSE")
