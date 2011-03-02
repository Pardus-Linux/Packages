#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--with-xml-parser=libxml\
                         --with-www=curl \
                         --disable-gtk-doc \
                         --with-html-dir=%s/html\
                         --disable-static" % docdir)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("%s/html" % docdir, "%s/%s/html/raptor/*" % (get.installDIR(), docdir))
    pisitools.removeDir("%s/html/raptor" % docdir)
    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
