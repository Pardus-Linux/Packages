#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    MINOR = "7"
    REL = "6"

    args = 'REAL_DAEMON_DIR=%s \
            RPM_OPT_FLAGS="%s -fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR" \
            LDFLAGS="%s -pie" \
            MAJOR=0 MINOR=%s REL=%s linux' % (get.sbinDIR(), get.CFLAGS(), get.LDFLAGS(), MINOR, REL)

    autotools.make('%s' % args)

def install():
    for app in ["tcpd", "tcpdmatch", "safe_finger", "try-from"]:
        pisitools.dosbin(app)

    pisitools.insinto("/usr/include", "tcpd.h")

    pisitools.insinto("/usr/lib", "libwrap.so*")

    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.allow.5")
    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.deny.5")

    pisitools.doman("*.3", "*.5", "*.8")
    pisitools.remove("/usr/share/man/man8/tcpdchk.*")

    pisitools.dodoc("BLURB", "CHANGES", "DISCLAIMER", "README*")

