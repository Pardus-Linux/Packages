#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import texlivemodules

WorkDir= "xmltex/base"

def build():
    texlivemodules.buildFormatFiles()

def install():
    pisitools.insinto("/var/lib/texmf", "texmf-var/*")

    for i in ["xmt", "cfg", "xml", "tex"]:
        pisitools.insinto("/usr/share/texmf-site/tex/xmltex/base/", "*.%s" %i)

    pisitools.insinto("/usr/share/texmf-site/tex/xmltex/config/", "*.ini")

    texlivemodules.createSymlinksFormat2Engines()

    pisitools.insinto("/etc/texmf/fmtutil.d/", "texmf/fmtutil/format.xmltex.cnf")

    pisitools.dodoc("readme.txt")
    pisitools.dohtml("*.html")

    pisitools.remove("/var/lib/texmf/web2c/pdftex/xmltex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/pdfxmltex.log")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/xmltex.fmt")
    pisitools.remove("/var/lib/texmf/web2c/pdftex/pdfxmltex.fmt")
