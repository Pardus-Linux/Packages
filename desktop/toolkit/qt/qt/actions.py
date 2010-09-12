#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4
from pisi.actionsapi import kde4

import os

WorkDir = "qt-everywhere-opensource-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')

qtbase = qt4.prefix
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

def setup():
    #make sure we don't use them
    for d in ('libjpeg', 'freetype', 'libpng', 'zlib', 'libtiff'):
        shelltools.unlinkDir("src/3rdparty/%s" % d)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PARDUS_CC" :       get.CC(),
            "PARDUS_CXX":       get.CXX(),
            "PARDUS_CFLAGS":    filteredCFLAGS,
            "PARDUS_LDFLAGS":   get.LDFLAGS()}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)

    #-no-pch makes build ccache-friendly
    autotools.rawConfigure("-no-pch \
                            -v \
                            -stl \
                            -fast \
                            -qdbus \
                            -qvfb \
                            -glib \
                            -no-sql-sqlite2 \
                            -system-sqlite \
                            -plugin-sql-sqlite \
                            -plugin-sql-mysql \
                            -plugin-sql-psql \
                            -plugin-sql-ibase \
                            -I/usr/include/mysql/ \
                            -I/usr/include/firebird/ \
                            -I/usr/include/postgresql/server/ \
                            -release \
                            -no-separate-debug-info \
                            -phonon \
                            -no-phonon-backend \
                            -webkit \
                            -no-rpath \
                            -openssl-linked \
                            -dbus-linked \
                            -xmlpatterns \
                            -opensource \
                            -reduce-relocations \
                            -prefix %s \
                            -libdir %s \
                            -docdir %s \
                            -examplesdir %s \
                            -demosdir %s\
                            -plugindir %s \
                            -translationdir %s \
                            -sysconfdir %s \
                            -datadir %s \
                            -importdir %s \
                            -headerdir %s \
                            -confirm-license " % (qt4.prefix, qt4.libdir, qt4.docdir, qt4.examplesdir, qt4.demosdir, qt4.plugindir, qt4.translationdir, qt4.sysconfdir, qt4.datadir, qt4.importdir, qt4.includedir))

def build():
    autotools.make()

def install():
    qt4.install()
    pisitools.dodir(qt4.bindir)

    #Remove phonon, we use KDE's phonon but we have to build Qt with Phonon support for webkit and some other stuff
    pisitools.remove("%s/libphonon*" % qt4.libdir)
    pisitools.removeDir("%s/phonon" % qt4.includedir)
    pisitools.removeDir("%s/phonon_backend" % qt4.plugindir)
    pisitools.remove("%s/pkgconfig/phonon*" % qt4.libdir)
    pisitools.remove("/usr/share/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml")
    os.removedirs("%s/usr/share/dbus-1/interfaces" % get.installDIR())

    pisitools.remove("%s/phononbackends/gstreamer.desktop" % kde4.servicesdir)
    os.removedirs("%s/%s/phononbackends" % (get.installDIR(), kde4.servicesdir))

    # Turkish translations
    shelltools.export("LD_LIBRARY_PATH", "%s%s" % (get.installDIR(), qt4.libdir))
    shelltools.system("%s%s/lrelease l10n-tr/*.ts" % (get.installDIR(), qt4.bindir))
    pisitools.insinto(qt4.translationdir, "l10n-tr/*.qm")

    # Fix all occurances of WorkDir in pc files
    pisitools.dosed("%s%s/pkgconfig/*.pc" % (get.installDIR(), qt4.libdir), "%s/qt-x11-opensource-src-%s" % (get.workDIR(), get.srcVERSION()), qt4.prefix)

    mkspecPath = "%s/mkspecs" % qtbase

    for root, dirs, files in os.walk("%s%s" % (get.installDIR(), qtbase)):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common","qws","features","default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")

    # Remove useless image directory, images of HTML docs are in doc/html/images
    pisitools.removeDir("%s/src" % qt4.docdir)
