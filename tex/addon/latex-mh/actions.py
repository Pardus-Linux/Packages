#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "mh"

def build():
    for dtxdoc in shelltools.ls("*.dtx"):
        shelltools.system("tex ./%s" % dtxdoc)
    
    for insfile in shelltools.ls("."):
        if insfile.endswith("ins"):
            shelltools.system("latex --interaction=batchmode %s" % insfile)


def install():
    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("dvi", "ps", "pdf")):
            pisitools.dodoc(srcfile)
            pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), srcfile), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, srcfile))
        elif srcfile.endswith(("sty", "cls", "fd", "clo", "def", "cfg")):
            pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, srcfile)

    pisitools.insinto("/usr/share/texmf-site/tex/latex/%s" % WorkDir, "*.sym")

    pisitools.dodoc("README")
