#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share"]

import os

def setup():
    # PAM files are named kde4.pam and kde4-np.pam. We should change cmake file to make PAM modules work
    #                      -DKDE4_ENABLE_FINAL=1 \
    kde4.configure("-DKDE4_COMMON_PAM_SERVICE=kde4 \
                          -DDBUS_SYSTEM_SERVICES_INSTALL_DIR=/usr/share/dbus-1/system-services \
                          -DKDE4_KCHECKPASS_PAM_SERVICE=kde4")

def build():
    kde4.make()

def install():
    # Do not use existing system KDM while creating the new one
    shelltools.export("GENKDMCONF_FLAGS", "--no-old")
    kde4.install()

    pisitools.dodir("/var/lib/kdm")

    shelltools.cd("build")

    # Copy desktop files into xsessions directory
    pisitools.insinto("/usr/share/xsessions", "kdm/kfrontend/sessions/kde*.desktop")

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("/usr/share/kde4/config/kdm/kdmrc", "/etc/X11/kdm/", "kdmrc")
    pisitools.dosym("/etc/X11/kdm/kdmrc", "/usr/share/kde4/config/kdm/kdmrc")

    # Use common Xsession script
    pisitools.remove("/usr/share/kde4/config/kdm/Xsession")
    pisitools.dosym("/usr/lib/X11/xinit/Xsession", "/usr/share/kde4/config/kdm/Xsession")
