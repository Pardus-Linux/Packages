#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import texlivemodules

def setup():
    pisitools.dosed('Makefile','tex -ini','latex -ini')

def build():
    shelltools.export("VARTEXFONTS", "%s/fonts" % get.curDIR())
    autotools.make()
    shelltools.export("VARTEXFONTS", "%s/fonts" % get.curDIR())
    shelltools.export("TEXMFHOME", "%s" % get.srcDIR())
    shelltools.system("env -u TEXINPUTS fmtutil --cnffile texmf/fmtutil/format.jadetex.cnf --fmtdir texmf-var/web2c --all")

def install():
    for runfiles in ["dsssl.def" ,"jadetex.ltx" , "jadetex.cfg", "jadetex.ini"]:
            pisitools.insinto("/usr/share/texmf/tex/jadetex" , runfiles)

    for styfiles in shelltools.ls(get.curDIR()):
        if styfiles.endswith("sty"):
            pisitools.insinto("/usr/share/texmf/tex/jadetex" , styfiles)

    pisitools.insinto("/var/lib/texmf" , "texmf-var/*")

    # The fotmat.jadetex.cnf is copied to texmf/fmtutil/ (see pspec.xml) , thus we can use the function below
    texlivemodules.createSymlinksFormat2Engines()

    pisitools.dodoc("ChangeLog*")
    pisitools.doman("*.1")
    pisitools.dohtml("index.html")
