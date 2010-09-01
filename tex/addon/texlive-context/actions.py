#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import texlivemodules

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[-1])
def build():
    texlivemodules.compile()

def install():
    pisitools.dosym("%s/%s/texmf-dist/scripts/context/ruby/texmfstart.rb" % (get.workDIR(),WorkDir), "/usr/bin/texmfstart")

    for i in ["context", "ctxtools", "exatools", "luatools", "makempy", "mpstools", "mptopdf", "mtxrun", "mtxtools", "pdftools", "pdftrimwhite", "pstopdf", "rlxtools", "runtools", "texexec", "texfind", "texfont" ,"texshow", "textools", "texutil", "tmftools", "xmltools"]:
        pisitools.dosym("%s/%s/texmf-dist/scripts/context/stubs/unix/%s" % (get.workDIR(), WorkDir, i), "/usr/bin/%s" % i)

    texlivemodules.install()

