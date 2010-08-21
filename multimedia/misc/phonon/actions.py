#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().partition("_")[0])

def setup():
    cmaketools.configure()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    """
    #move kde related stuff to KDE dirs
    pisitools.dodir("/usr/kde/4/lib/kde4/plugins/phonon_backend")
    pisitools.domove("%s/lib/kde4/plugins/phonon_backend/*" % qtPrefix, "/usr/kde/4/lib/kde4/plugins/phonon_backend")

    pisitools.dodir("/usr/kde/4/share/kde4/services/phononbackends")
    pisitools.domove("%s/share/kde4/services/phononbackends/*" % qtPrefix, "%s/share/kde4/services/phononbackends" % kdePrefix)

    #pure Qt4 apps look for this path to use phonon backends
    pisitools.dodir("%s/plugins/phonon_backend" % qtPrefix)
    pisitools.dosym("%s/lib/kde4/plugins/phonon_backend/phonon_gstreamer.so" % kdePrefix, "%s/plugins/phonon_backend/libphonon_gstreamer.so" % qtPrefix)
    pisitools.dosym("%s/lib/kde4/plugins/phonon_backend/phonon_xine.so" % kdePrefix, "%s/plugins/phonon_backend/libphonon_xine.so" % qtPrefix)
    """

    #some applications like mediaplayer example of Qt needs this #11648
    pisitools.dosym("/usr/include/KDE/Phonon", "/usr/include/Phonon")
