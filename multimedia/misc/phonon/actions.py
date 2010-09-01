#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import qt4
from pisi.actionsapi import kde4

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().partition("_")[0])

def setup():
    cmaketools.configure()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pure Qt4 apps look for this path to use phonon backends
    pisitools.dodir("%s/phonon_backend" % qt4.plugindir)
    pisitools.dosym("%s/plugins/phonon_backend/phonon_gstreamer.so" % kde4.modulesdir, "%s/phonon_backend/libphonon_gstreamer.so" % qt4.plugindir)
    pisitools.dosym("%s/plugins/phonon_backend/phonon_xine.so" % kde4.modulesdir, "%s/phonon_backend/libphonon_xine.so" % qt4.plugindir)

    #some applications like mediaplayer example of Qt needs this #11648
    pisitools.dosym("/usr/include/KDE/Phonon", "/usr/include/Phonon")
