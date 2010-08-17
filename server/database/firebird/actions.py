#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="Firebird-%s-0" % get.srcVERSION()

def setup():
    shelltools.chmod("./src/misc/writeBuildNum.sh")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/opt/firebird \
                         --disable-static \
                         --enable-superserver \
                         --with-system-icu \
                         --with-editline")

def build():
    #Parallel build is broken
    autotools.make("-j1")
    shelltools.cd("gen")
    autotools.make("-f Makefile.install buildRoot")

def install():
    # Copy to install directory
    shelltools.copytree("gen/buildroot/", get.installDIR())

    # Move headers
    pisitools.remove("/usr/include/*")
    pisitools.domove("/opt/firebird/include", "/usr/include", "firebird")

    # Fix client libraries symlinks
    pisitools.remove("/usr/lib/*")
    for libs in os.listdir("%s/opt/firebird/lib" % get.installDIR()):
        pisitools.dosym("/opt/firebird/lib/%s" % libs, "/usr/lib/%s" % libs)

    # Add support for old client's
    pisitools.dosym("libfbclient.so", "/usr/lib/libgds.so")
    pisitools.dosym("libfbclient.so", "/usr/lib/libgds.so.0")
    pisitools.dosym("libfbclient.so", "/opt/firebird/lib/libgds.so")
    pisitools.dosym("libfbclient.so", "/opt/firebird/lib/libgds.so.0")

    # Move configuration files and security DB to /etc/firebird for painless upgrade
    pisitools.domove("/opt/firebird/aliases.conf", "/etc/firebird")
    pisitools.domove("/opt/firebird/firebird.conf", "/etc/firebird")
    pisitools.domove("/opt/firebird/security2.fdb", "/etc/firebird")
    pisitools.dosym("/etc/firebird/aliases.conf", "/opt/firebird/aliases.conf")
    pisitools.dosym("/etc/firebird/firebird.conf", "/opt/firebird/firebird.conf")
    pisitools.dosym("/etc/firebird/security2.fdb", "/opt/firebird/security2.fdb")

    # Set PID directory
    shelltools.makedirs("%s/var/run/firebird" % get.installDIR())
    #pisitools.dodir("/opt/firebird/run")

    # Set permissions
    shelltools.chmod("%s/etc/firebird/security2.fdb" % get.installDIR(), 0600)
    shelltools.chmod("%s/var/run/firebird" % get.installDIR(), 0755)
    #shelltools.chmod("%s/opt/firebird/run" % get.installDIR(), 0755)

    pisitools.dosym("/var/log/firebird.log", "/opt/firebird/firebird.log")

    # Useless init.d stuff
    pisitools.removeDir("/opt/firebird/misc/")

    # Prevent to conflict isql with UnixODBC's
    pisitools.domove("/opt/firebird/bin/isql", "/opt/firebird/bin", "fb_isql")
