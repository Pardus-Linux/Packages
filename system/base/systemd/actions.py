#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-rootdir= \
                         --with-distro=pardus \
                         --disable-gtk")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Create SysV compatibility symlinks
    pisitools.dodir("/sbin")
    pisitools.dosym("/bin/systemd", "/sbin/init")

    for bin in ("reboot", "halt", "poweroff",
                "shutdown", "telinit", "runlevel"):
        pisitools.dosym("/bin/systemctl", "/sbin/%s" % bin)

    # Make sure these dirs are owned by systemd
    for d in ("basic", "default", "dbus", "syslog"):
        pisitools.dodir("/lib/systemd/system/%s.target.wants" % d)

    # Create new style configuration files
    # FIXME: These will cause pisi to bork during pisi check
    #for f in ("hostname", "vconsole.conf", "locale.conf",
    #          "machine-id", "machine-info", "timezone"):
    #    shelltools.touch("%s/etc/%s" % (get.installDIR(), f))

    # Create directories
    for d in ("tmpfiles.d", "sysctl.d", "binfmt.d", "modules-load.d"):
        pisitools.dodir("/etc/%s" % d)


    pisitools.dodoc("LICENSE", "README")
