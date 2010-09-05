#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
import os

WorkDir="feynmf-%s" % get.srcVERSION()
shelltools.export("VARTEXFONTS", get.curDIR())

def build():
    autotools.make("MP=mpost all manual.ps")
    autotools.make("-f Makefile.cnl ps")

def install():
    pisitools.insinto("/usr/bin/", "feynmf.pl", "feynmf")
    pisitools.doman("feynmf.1")
    for i in ["feynmf.sty", "feynmp.sty"]:
        pisitools.insinto("/usr/share/texmf-site/tex/latex/feynmf", i)
    for i in ["feynmf.mf", "feynmp.mp"]:
        pisitools.insinto("/usr/share/texmf-site/metafont/feynmf", i)
    pisitools.dodoc("README", "manual.ps", "template.tex", "fmfcnl*.ps")
