#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="clucene-core-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-multithreading \
                         --disable-debug \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/include/CLucene/","src/CLucene/clucene-config.h")
    pisitools.removeDir("/usr/lib/CLucene/")

    pisitools.dodoc("AUTHORS","README","COPYING","ChangeLog")
