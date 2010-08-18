#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("wpa_supplicant")

    autotools.make()
    autotools.make("eapol_test")

def install():
    shelltools.cd("wpa_supplicant")

    for bin in ["wpa_supplicant", "wpa_cli", "wpa_passphrase", "eapol_test"]:
        pisitools.dosbin(bin)

    pisitools.dodir("/var/run/wpa_supplicant")

    # Install dbus files
    pisitools.insinto("/usr/share/dbus-1/system-services", "dbus-wpa_supplicant.service", "fi.epitest.hostap.WPASupplicant.service")
    pisitools.insinto("/etc/dbus-1/system.d", "dbus-wpa_supplicant.conf", "wpa_supplicant.conf")

    pisitools.doman("doc/docbook/*.5")
    pisitools.doman("doc/docbook/*.8")
    pisitools.newdoc("wpa_supplicant.conf", "wpa_supplicant.conf.example")

    pisitools.dodoc("ChangeLog", "../COPYING", "eap_testing.txt", "../README", "todo.txt", "examples/*")
