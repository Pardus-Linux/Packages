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

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    pisitools.dosed("alsactl/init/Makefile.in", "^alsainitdir = .*$", "alsainitdir = /lib/alsa/init")

    autotools.configure("--enable-nls \
                         --disable-alsaconf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/sbin/alsactl", "/sbin/alsactl")
    pisitools.dosym("/lib/alsa/init", "/usr/share/alsa/init")

    pisitools.dodir("/etc")
    shelltools.touch("%s/etc/asound.state" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "TODO", "seq/aconnect/README.aconnect", "seq/aseqnet/README.aseqnet")
