#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CFLAGS=-Os -fomit-frame-pointer -s -pipe")

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.rawInstall("DESTPREFIX=%s/usr" % get.installDIR())
    pisitools.removeDir("/usr/share/doc/%s-%s" % (get.srcNAME(), get.srcVERSION()))

    pisitools.dodoc("SCHED_DESIGN", "CHANGES", "LICENSE", "README", "TUNING")
