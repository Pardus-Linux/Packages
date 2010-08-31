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
    shelltools.cd("%s/source/" % GetWorkdir)
    shelltools.export("LC_ALL","C")


def build():
    shelltools.makedirs("%s/build" % GetWorkdir)
    shelltools.cd("%s/build/" % GetWorkdir)

    conf_options =  "--enable-cxx-runtime-hack \
                    --disable-all-pkgs \
                    --enable-shared    \
                    --disable-largefile \
                    --disable-native-texlive-build \
                    --disable-ptex \
                    --disable-ipc \
                    --enable-dump-share  \
                    --enable-mp  \
                    --enable-luatex  \
                    --with-system-ptexenc \
                    --with-system-kpathsea \
                    --with-system-poppler \
                    --with-system-xpdf \
                    --with-system-freetype \
                    --with-system-freetype2 \
                    --with-system-gd \
                    --with-system-libpng \
                    --with-system-teckit \
                    --with-system-t1lib \
                    --with-system-zlib \
                    --with-system-icu \
                    --without-system-zziplib \
                    --without-mf-x-toolkit --without-x"

    shelltools.system('TL_MAKE="make" ../source/configure %s' % conf_options)

def install():
    shelltools.cd("%s/build/" % GetWorkdir)
    autotools.rawInstall("DESTDIR=%s bin_PROGRAMS='luatex' SUBDIRS='' nodist_man_MANS=''" % get.installDIR()) 
    
    pisitools.dodoc("%s/README" % GetWorkdir, "%s/manual/*.pdf" % GetWorkdir)


