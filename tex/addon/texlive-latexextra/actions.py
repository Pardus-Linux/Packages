#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import texlivemodules

from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[-1])

def build():
    texlivemodules.compile()

def install():
    texlivemodules.install()

    # Install texmf bin scripts
    pisitools.dosym("/usr/share/texmf-dist/scripts/perltex/perltex.pl", "/usr/bin/perltex" )
    pisitools.dosym("/usr/share/texmf-dist/scripts/ppower4/pdfthumb.texlua", "/usr/bin/pdfthumb" )
    pisitools.dosym("/usr/share/texmf-dist/scripts/ppower4/ppower4.texlua", "/usr/bin/ppower4" )
    pisitools.dosym("/usr/share/texmf-dist/scripts/pst-pdf/ps4pdf", "/usr/bin/ps4pdf" )
    pisitools.dosym("/usr/share/texmf-dist/scripts/vpe/vpe.pl", "/usr/bin/vpe" )
