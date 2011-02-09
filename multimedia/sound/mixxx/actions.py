#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "~"))


def build():
    shelltools.export("LINKFLAGS", get.LDFLAGS())
    scons.make("prefix=/usr \
                install_root=%s/usr \
                qtdir=%s \
                djconsole=1 \
                portmidi=0 \
                optimize=1 \
                script=1 \
                shoutcast=1 \
                tonal=1 \
                m4a=1 \
                ladspa=1 \
                ipod=1" % (get.installDIR(), get.qtDIR()))

def install():
    shelltools.export("LINKFLAGS", get.LDFLAGS())
    scons.install("install prefix=/usr \
                   install_root=%s/usr \
                   qtdir=%s \
                   djconsole=1 \
                   portmidi=0 \
                   optimize=1 \
                   script=1 \
                   shoutcast=1 \
                   tonal=1 \
                   m4a=1 \
                   ladspa=1 \
                   ipod=1" % (get.installDIR(), get.qtDIR()))

    pisitools.dodoc("README*", "COPYING", "Mixxx-Manual.pdf")
