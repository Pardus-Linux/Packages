#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

# 0.8.5 is a patch over 0.8.1
WorkDir = "openarena-engine-0.8.1"
#WorkDir = "openarena-engine-%s" % get.srcVERSION()
builddir = "build/release-linux-%s" % get.ARCH()
datadir = "/usr/share/openarena"

def build():
    autotools.make('OPTIMIZE="%s" \
                    DEFAULT_BASEDIR="%s" \
                    BUILD_STANDALONE=1 \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    USE_SDL=1 \
                    USE_OPENAL=1 \
                    USE_CURL=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_LOCAL_HEADERS=1' % (get.CFLAGS(), datadir))

def install():
    pisitools.insinto("/usr/bin", "%s/oa_ded.%s" % (builddir, get.ARCH()), "openarena-server")
    pisitools.insinto("/usr/bin", "%s/openarena.%s" % (builddir, get.ARCH()), "openarena")
    pisitools.insinto("/usr/bin", "%s/openarena-smp.%s" % (builddir, get.ARCH()), "openarena-smp")

    pisitools.dodoc("BUGS", "ChangeLog", "NOTTODO", "TODO", "README", "*.txt")
