#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    #Remove egg-type reportlab dependency, we have dependency feature in Pisi AFAIK :)
    pisitools.remove("/usr/lib/%s/site-packages/rst2pdf-*egg-info/requires.txt" % get.curPYTHON())

    pisitools.dodoc("doc/manual.txt", "LICENSE.txt", "README.txt", "Contributors.txt")
    pisitools.doman("doc/rst2pdf.1")
