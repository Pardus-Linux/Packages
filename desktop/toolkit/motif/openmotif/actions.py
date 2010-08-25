#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

mwmlibdir = "/usr/lib/X11"
mwmconfigdir = "/etc/X11/mwm"

def setup():
    # add X.Org vendor string to aliases for virtual bindings
    shelltools.echo("bindings/xmbind.alias", '"The X.Org Foundation"\t\t\t\t\tpc')

    # libXp will be deprecated
    pisitools.dosed("lib/Xm/Makefile.am", " -lXp ", " -ldeprecatedXp ")

    shelltools.export("LANG", "C") # guess why this is here...
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-strict-aliasing" % get.CXXFLAGS())
    shelltools.export("AT_M4DIR", ".")

    for f in ["NEWS", "AUTHORS"]:
        shelltools.touch(f)

    autotools.autoreconf("-vfi")
    autotools.configure("--with-x \
                         --disable-static \
                         --enable-utf8 \
                         --enable-xft \
                         --enable-jpeg \
                         --enable-png")

def build():
    autotools.make('-j1 MWMRCDIR="/etc/X11/mwm"')

def install():
    autotools.rawInstall('DESTDIR=%s -j1 MWMRCDIR="/etc/X11/mwm"' % get.installDIR())

    # pisitools.domove("%s/system.mwmrc" % mwmlibdir, "%s/" % mwmconfigdir)
    # pisitools.dosym("%s/system.mwmrc" % mwmconfigdir, "%s/system.mwmrc" % mwmlibdir)

    # these are just demos
    pisitools.removeDir("/usr/share/Xm")
    pisitools.dodoc("ChangeLog", "README*", "BUGREPORT", "RELEASE", "RELNOTES", "TODO")

