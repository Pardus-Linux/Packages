#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "dvd-slideshow-0.8.2-2"

def install():
    pisitools.dobin("dvd-slideshow")
    pisitools.dobin("dvd-menu")
    pisitools.dobin("dvd-burn")
    pisitools.dobin("gallery1-to-slideshow")
    pisitools.dobin("jigl2slideshow")
    pisitools.dobin("dir2slideshow")
    pisitools.doman("man/*")
    pisitools.dodoc("COPYING.txt", "TODO.txt", "INSTALL.txt")
    pisitools.dohtml("doc/*.html")
