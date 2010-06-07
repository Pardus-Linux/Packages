#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="pcre-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-utf8 \
                         --enable-unicode-properties \
                         --with-link-size=2 \
                         --with-match-limit=10000000 \
                         --enable-newline-is-lf \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
