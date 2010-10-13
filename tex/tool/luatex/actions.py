#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import cmaketools

WorkDir = "luatex-beta-%s" % get.srcVERSION()
GetWorkdir = "%s/%s" % (get.workDIR(), WorkDir)


def setup():
    libtools.libtoolize()
    shelltools.export("LC_ALL","C")
    shelltools.cd("%s/source/texk/web2c" % GetWorkdir)

    autotools.configure("--disable-cxx-runtime-hack \
                        --disable-afm2pl    \
                        --disable-aleph		\
                        --disable-bibtex	\
                        --disable-bibtex8	\
                        --disable-cfftot1	\
                        --disable-cjkutils	\
                        --disable-detex		\
                        --disable-devnag	\
                        --disable-dialog	\
                        --disable-dtl		\
                        --enable-dump-share	\
                        --disable-dvi2tty	\
                        --disable-dvidvi	\
                        --without-dviljk    \
                        --disable-dvipdfm	\
                        --disable-dvipdfmx	\
                        --disable-dvipos	\
                        --disable-dvipsk	\
                        --disable-gsftopk	\
                        --disable-ipc		\
                        --disable-lacheck	\
                        --disable-lcdf-typetools \
                        --disable-makeindexk \
                        --disable-mf		\
                        --disable-mmafm		\
                        --disable-mmpfb		\
                        --disable-mp		\
                        --disable-musixflx	\
                        --disable-otfinfo	\
                        --disable-otftotfm	\
                        --disable-pdfopen	\
                        --disable-pdftex	\
                        --disable-ps2eps	\
                        --disable-ps2pkm	\
                        --disable-psutils	\
                        --disable-ptex		\
                        --disable-seetexk	\
                        --disable-t1dotlessj  \
                        --disable-t1lint	\
                        --disable-t1rawafm	\
                        --disable-t1reencode	\
                        --disable-t1testpage \
                        --disable-t1utils	\
                        --disable-tex		\
                        --disable-tex4htk	\
                        --disable-tpic2pdftex	\
                        --disable-ttf2pk	\
                        --disable-ttfdump	\
                        --disable-ttftotype42	\
                        --disable-vlna		\
                        --disable-web-progs \
                        --disable-xdv2pdf	\
                        --disable-xdvipdfmx \
                        --disable-xetex		\
                        --without-x			\
                        --with-system-kpathsea	\
                        --with-system-gd	\
                        --with-system-libpng	\
                        --with-system-teckit \
                        --with-system-zlib \
                        --with-system-t1lib \
                        --with-system-xpdf \
                        --with-system-zziplib \
                        --disable-largefile \
                        --disable-multiplatform \
                        --disable-shared")

    for i in ["libs/obsdcompat", "texk/kpathsea"]:
        shelltools.cd("%s/source/%s" % (GetWorkdir, i))
        autotools.configure()

def build():
    for i in ["libs/obsdcompat", "texk/kpathsea"]:
        shelltools.cd("%s/source/%s" % (GetWorkdir, i))
        autotools.make()

    shelltools.cd("%s/source/texk/web2c" % GetWorkdir)
    autotools.make()

def install():
    shelltools.cd("%s/source/texk/web2c" % GetWorkdir)

    autotools.rawInstall("DESTDIR=%s bin_PROGRAMS='luatex' SUBDIRS='' nodist_man_MANS=''" % get.installDIR()) 

    pisitools.dodoc("%s/README" % GetWorkdir, "%s/manual/*.pdf" % GetWorkdir)
