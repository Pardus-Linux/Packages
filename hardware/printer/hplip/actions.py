#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    # Patch compressed PPDs
    for patch in sorted(os.listdir("ppd-patches")):
        shelltools.system("./patch-ppds ppd-patches/%s" % patch)

    for f in ("NEWS", "INSTALL", "README", "AUTHORS", "ChangeLog"):
        shelltools.touch(f)

    autotools.autoreconf("-fi")

    # Strip duplex constraints from hpcups
    pisitools.dosed("prnt/drv/hpcups.drv.in", "(UIConstraints.* \*Duplex)", "//\\1")

    # These are barely the defaults except:
    # --enable-foomatic-drv-install (default=no) (respected by Fedora, enabled by Ubuntu)
    autotools.configure("--with-cupsbackenddir=/usr/lib/cups/backend \
                         --with-drvdir=/usr/share/cups/drv \
                         --with-hpppddir=/usr/share/cups/model/hplip \
                         --with-docdir=/usr/share/doc/hplip \
                         --disable-qt3 \
                         --disable-policykit \
                         --enable-qt4 \
                         --enable-hpijs-install \
                         --enable-udev-acl-rules \
                         --enable-pp-build \
                         --enable-doc-build \
                         --enable-fax-build \
                         --enable-gui-build \
                         --enable-dbus-build \
                         --enable-scan-build \
                         --enable-network-build \
                         --enable-hpcups-install \
                         --enable-new-hpcups \
                         --enable-cups-drv-install \
                         --enable-foomatic-drv-install \
                         --disable-doc-build \
                         --disable-foomatic-ppd-install \
                         --disable-foomatic-rip-hplip-install")

    # Remove hardcoded rpaths
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s ppddir=/usr/share/cups/model/hplip" % get.installDIR())

    # Create a compatibility symlink for foomatic-rip-hplip
    pisitools.dosym("/usr/lib/cups/filter/foomatic-rip", "/usr/lib/cups/filter/foomatic-rip-hplip")

    # Remove the hal preprobe rules as they were causing breakage (bug #479648).
    # Remove hal directory as well.
    pisitools.removeDir("/usr/share/hal/")

    # Do not mess with sane, init, foomatic etc.
    pisitools.removeDir("/etc/sane.d")

    # Create empty plugins directory
    pisitools.dodir("/usr/share/hplip/prnt/plugins")

    # This notifies user through libnotify when the printer requires a firmware
    # Should port it to KNotify if possible, argh.
    pisitools.remove("/lib/udev/rules.d/56-hpmud_support.rules")

    # The systray applet doesn't work properly (displays icon as a
    # window), so don't ship the launcher yet.
    pisitools.removeDir("/etc/xdg/")

    # --disable-doc-build used. It doesn't go to the true directory.
    pisitools.dohtml("doc/*")
