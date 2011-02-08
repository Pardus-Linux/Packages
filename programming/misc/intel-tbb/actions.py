#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="tbb%soss" % (get.srcVERSION().replace(".", ""))

def build():
    autotools.make("CXXFLAGS='%s' tbb_build_prefix=obj" % get.CXXFLAGS())

def install():
    shelltools.system("./install.sh %s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
