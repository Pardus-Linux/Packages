#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ruby-%s" % get.srcVERSION().replace("_","-")

def setup():
    autotools.configure("--enable-shared \
                         --enable-pthread \
                         --enable-doc \
                         --enable-ipv6 \
                         --disable-rpath \
                         --with-sitedir=/usr/lib/ruby/site_ruby")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-doc" % get.installDIR())

    pisitools.dodoc("COPYING*", "ChangeLog", "README*", "ToDo")
