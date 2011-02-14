#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Pyro-%s" % get.srcVERSION()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME() ,"examples")
    pisitools.dohtml("docs/*")
    pisitools.dodoc("LICENSE", "Pyro.conf", "README.txt")
