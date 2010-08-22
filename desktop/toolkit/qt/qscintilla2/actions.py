#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import qt4

WorkDir = "QScintilla-gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]

def setup():
    shelltools.cd("Qt4/")
    qt4.configure()

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4/")
    qt4.configure()

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())
    #pisitools.dosed("Makefile", "\\$\\(SUBLIBS\\)  -L/usr/qt/4/lib", "$(SUBLIBS)")

def build():
    shelltools.cd("Qt4/")
    autotools.make("all staticlib CC=\"%s\" CXX=\"%s\" LINK=\"%s\"" % (get.CC(), get.CXX(), get.CXX()))

    shelltools.cd("../designer-Qt4/")
    autotools.make("DESTDIR=\"%s/%s/designer\"" % (get.installDIR(), qt4.plugindir))

    # Get Makefile of qscintilla-python via sip
    shelltools.cd("../Python")
    pythonmodules.run("configure.py -p 4 -n ../Qt4 -o ../Qt4")
    autotools.make()

def install():
    # installs not managed by the build system
    shelltools.cd("Qt4/")
    #pisitools.insinto("/%s/lib" % Qt4DIR, "libqscintilla2.so*")
    pisitools.dolib("libqscintilla2.so*")

    #shelltools.makedirs("%s/%s/include" % (get.installDIR(), Qt4DIR))
    pisitools.dodir("/usr/include")
    shelltools.copytree("Qsci", "%s/usr/include/Qsci" % get.installDIR())
    pisitools.insinto(qt4.translationdir, "qscintilla*.qm")

    shelltools.cd("../")
    pisitools.insinto("%s/designer" % qt4.plugindir, "designer-Qt4/libqscintillaplugin.so")

    #build and install qscintilla-python
    shelltools.cd("Python")
    autotools.install("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

    pisitools.dodoc("GPL*", "LICENSE*", "NEWS", "README", "OPENSOURCE-NOTICE.TXT")
