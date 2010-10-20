#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

datadir = "/usr/share/alienarena"
libdir = "/usr/lib/alienarena"

def setup():
    # Use system GL header
    pisitools.dosed("source/ref_gl/r_local.h", "glext.h", "GL/glext.h")

def build():
    shelltools.cd("source")
    autotools.make("CC=%s \
                    PREFIX=/usr \
                    BUILD=ALL \
                    OPTIM_LVL=2 \
                    SDLSOUND=yes \
                    WITH_DATADIR=yes \
                    WITH_LIBDIR=yes \
                    DATADIR=%s \
                    LIBDIR=%s \
                    OPTIMIZED_CFLAGS=no" % (get.CC(), datadir, libdir))

def install():
    shelltools.cd("source")
    pisitools.dobin("release/crded")
    pisitools.dobin("release/crx")

    pisitools.rename("/usr/bin/crded", "alienarena-server")
    pisitools.rename("/usr/bin/crx", "alienarena")

    pisitools.doexe("release/game.so", "%s/arena" % libdir)
