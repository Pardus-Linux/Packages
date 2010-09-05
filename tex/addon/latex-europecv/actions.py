#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "europecv"

def build():
    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("tex", "dtx")):
            shelltools.system("texi2dvi -q -c --language=latex %s" % srcfile)

def install():
    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("dvi", "ps", "pdf")):
            pisitools.dodoc(srcfile)
            pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), srcfile), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, srcfile))
        elif srcfile.endswith(("sty", "cls", "fd", "clo", "def", "cfg")):
            pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, srcfile)


    for i in ["ecv*", "europecv.cls", "EuropeFlag*", "europasslogo*"]:
        pisitools.insinto("/usr/share/texmf-site/tex/latex/%s" % WorkDir, i)

    pisitools.dodoc("europecv.pdf", "europecv.tex", "examples/*", "templates/*")
    pisitools.dosym("/usr/share/doc/%s/europecv.pdf" % get.srcTAG(), "/usr/share/texmf-site/doc/latex/%s/europecv.pdf" % WorkDir)
