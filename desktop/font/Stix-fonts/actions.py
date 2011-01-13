#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="Stix"

def install():
    shelltools.chmod("*.ttf",0644)

    pisitools.insinto("/usr/share/fonts/stix","*.ttf")

    pisitools.dosym("../conf.avail/stix-fonts-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-integrals-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-integrals-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-pua-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-pua-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-sizes-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-sizes-fontconfig.conf")
    pisitools.dosym("../conf.avail/stix-fonts-variants-fontconfig.conf", "/etc/fonts/conf.d/stix-fonts-variants-fontconfig.conf")
