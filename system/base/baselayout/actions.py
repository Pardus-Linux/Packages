# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    # NOTE: This is only for the start-stop-daemon
    autotools.make('-C src CC="%s" LD="%s %s" CFLAGS="%s"' % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    pisitools.insinto("/", "root/*")

    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)

    shelltools.echo("%s/etc/pardus-release" % get.installDIR(), "Pardus 2011 Alpha 2")

    # Install baselayout documentation
    pisitools.doman("man/*.*")

    # Install baselayout utilities
    shelltools.cd("src/")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # NOTE: We should not need this these days
    #chmod("/mnt/floppy", 0700)

    # FIXME: Check these if we switch to systemd
    chmod("/tmp", 01777)
    chmod("/var/lock", 0755)
    chmod("/var/tmp", 01777)
    chmod("/usr/share/baselayout/shadow", 0600)

    # FHS compatibility symlinks stuff
    pisitools.dosym("/var/tmp", "/usr/tmp")
    pisitools.dosym("share/man", "/usr/local/man")

    if get.ARCH() == "x86_64":
        # Hack for binary blobs built on multi-lib systems
        pisitools.dosym("lib", "/lib64")
