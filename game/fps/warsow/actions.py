#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "./"
source = "source"
#arch = "i386"
arch = "x86_64"

def build():
    shelltools.export("AR", "ar")
    shelltools.export("RANLIB", "ranlib")

    shelltools.cd(source)

    autotools.make("-C ../libsrcs/angelscript/angelSVN/sdk/angelscript/projects/gnuc")
    autotools.make('BINDIR=release \
                    BUILD_CLIENT=YES \
                    BUILD_SERVER=YES \
                    BUILD_IRC=YES \
                    BUILD_SND_QF=YES \
                    BUILD_SND_OPENAL=YES \
                    BUILD_TV_SERVER=YES \
                    BUILD_ANGELWRAP=YES \
                    DEBUG_BUILD=YES \
                    BASE_ARCH=%s \
                    CFLAGS_RELEASE="%s -DNDEBUG" \
                    CC="%s" \
                    all' % (arch, get.CFLAGS(), get.CC()))

                    #shell scripts override these, disabling for now
                    #SERVER_EXE=warsow-server \
                    #CLIENT_EXE=warsow \


def install():
    for i in ["doc", "rtf", "txt"]:
        pisitools.dodoc("docs/*.%s" % i)
    shelltools.cd(source)

    pisitools.insinto("/usr/bin", "release/warsow.%s" % arch, "warsow")
    pisitools.insinto("/usr/bin", "release/wsw_server.%s" % arch, "warsow-server")
    pisitools.insinto("/usr/bin", "release/wswtv_server.%s" % arch, "warsowtv-server")

    pisitools.dodir("/usr/share/warsow")
    pisitools.insinto("/usr/share/warsow/", "release/basewsw")
    pisitools.insinto("/usr/share/warsow/", "release/libs")

