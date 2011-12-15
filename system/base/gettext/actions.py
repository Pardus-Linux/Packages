#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

shelltools.export("LC_ALL", "C")

def setup():
    # autoreconf breaks linker, graaaaaaaaggggghhhhhhh
    # External glib and croco generates cyclic dependency hell between glib, croco and gettext
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-java \
                         --disable-native-java \
                         --disable-csharp \
                         --disable-git \
                         --disable-rpath \
                         --disable-static \
                         --disable-openmp \
                         --without-included-gettext \
                         --without-emacs \
                         --with-included-libcroco \
                         --with-included-glib \
                         --with-included-libxml \
                         --with-pic=yes \
                         --enable-nls \
                         --enable-shared")

def build():
    autotools.make("GMSGFMT=../src/msgfmt")

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/%s/html" % (get.installDIR(), docdir))

    pisitools.doexe("gettext-tools/misc/gettextize", "/usr/bin")

    # Remove C# & Java stuff
    pisitools.remove("%s/html/examples/build-aux/csharp*" % docdir)
    pisitools.remove("%s/html/examples/build-aux/java*" % docdir)
    pisitools.removeDir("%s/html/examples/*java*" % docdir)
    pisitools.removeDir("%s/html/*java*" % docdir)

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "HACKING", "NEWS", "README*", "THANKS")

