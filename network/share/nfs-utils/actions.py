#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIE" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

    autotools.configure("--with-statedir=/var/lib/nfs \
                         --disable-gss \
                         --enable-nfsv4 \
                         --enable-nfsv3 \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/nfs")
    pisitools.dodir("/var/lib/nfs/statd")
    pisitools.dodir("/var/lib/nfs/sm")
    pisitools.dodir("/var/lib/nfs/sm.bak")
    pisitools.dodir("/var/lib/nfs/rpc_pipefs")
    pisitools.dodir("/var/lib/nfs/rpc_pipefs/nfs")
    pisitools.dodir("/var/lib/nfs/v4recovery")

    shelltools.touch("%s/var/lib/nfs/state" % get.installDIR())
    shelltools.touch("%s/var/lib/nfs/xtab" % get.installDIR())
    shelltools.touch("%s/var/lib/nfs/etab" % get.installDIR())
    shelltools.touch("%s/var/lib/nfs/rmtab" % get.installDIR())

    pisitools.domove("/usr/sbin/rpc.statd", "/sbin/")

    pisitools.dodoc("ChangeLog", "README")
