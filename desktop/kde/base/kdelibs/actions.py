#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4

NoStrip=["/usr/share"]
shelltools.export("HOME", get.workDIR())

def setup():
    #kde4.configure("-DKDE4_ENABLE_FINAL=ON -DKDE_DISTRIBUTION_TEXT=\"Pardus\"")
    kde4.configure("-DKDE_DISTRIBUTION_TEXT=\"Pardus\" -DCMAKE_INSTALL_TYPE=debugfull")

def build():
    kde4.make()

def install():
    kde4.install()

    #move Qt Designer plugins to Qt plugin directory
    pisitools.dodir("%s/designer" % qt4.plugindir)
    pisitools.domove("%s/plugins/designer/*" % kde4.modulesdir, "%s/designer" % qt4.plugindir)
    pisitools.removeDir("%s/plugins/designer" % kde4.modulesdir)

    #Use openssl CA list instead of the outdated KDE list
    pisitools.remove("%s/kssl/ca-bundle.crt" % kde4.appsdir)
    pisitools.dosym("/etc/pki/tls/certs/ca-bundle.crt", "%s/kssl/ca-bundle.crt" % kde4.appsdir)
