# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "js/src"

def build():
    autotools.make("-j1 -f Makefile.ref \
                    JS_THREADSAFE=1 \
                    CC=%s CCC=%s \
                    XCFLAGS='%s -fPIC -DJS_C_STRINGS_ARE_UTF8' \
                    XLDFLAGS='%s' \
                    BUILD_OPT='1'"
                    % (get.CC(), get.CXX(),
                       get.CFLAGS(), get.LDFLAGS()))

def install():
    # make is picky about the order of install
    autotools.make("-f Makefile.ref install DESTDIR=%s" % (get.installDIR()))

    pisitools.remove("/usr/lib/libjs.a")

    # Make versioned *.so and create needed symlinks
    pisitools.rename("/usr/lib/libjs.so", "libjs.so.1")
    pisitools.dosym("/usr/lib/libjs.so.1", "/usr/lib/libjs.so")

    pisitools.dodoc("../jsd/README")
    pisitools.dohtml("README.html")
