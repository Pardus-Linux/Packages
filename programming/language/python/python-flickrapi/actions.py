#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "flickrapi-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    shelltools.system("doxygen doc/GNUmakefile")

    pisitools.dohtml("html/*")

    pisitools.remove("/usr/README")
    pisitools.remove("/usr/UPGRADING")
    pisitools.remove("/usr/LICENSE")

    pisitools.removeDir("%s/flickrapi-%s" % (get.docDIR(), get.srcVERSION()))
