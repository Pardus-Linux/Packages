#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--without-rpmbuild \
                         --with-patch-wrapper \
                         --with-sendmail=/usr/sbin/sendmail \
                         --with-patch=/usr/bin/patch \
                         --with-diffstat=/usr/bin/diffstat")

def build():
    autotools.make("BUILD_ROOT=%s RELEASE=%s" % (get.installDIR(), get.srcRELEASE()))

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("BUILD_ROOT=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/emacs")
