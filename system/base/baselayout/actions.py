# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    autotools.make('-C src CC="%s" LD="%s %s" CFLAGS="%s"' % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    pisitools.insinto("/", "root/*")

    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)


    chmod("/etc/shadow", 0600)

    shelltools.echo("%s/etc/pardus-release" % get.installDIR(), "Pardus 2011 Alpha 2")

    # Install some files to /usr/share/baselayout instead of /etc to keep from overwriting the user's settings,
    for f in ("passwd", "shadow", "group", "fstab", "hosts", "ld.so.conf", "resolv.conf", "inittab.live"):
        pisitools.domove("/etc/%s" % f, "/usr/share/baselayout")

    # Install baselayout documentation
    pisitools.doman("man/*.*")

    # Install baselayout utilities
    shelltools.cd("src/")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    chmod("/mnt/floppy", 0700)
    chmod("/tmp", 01777)
    chmod("/var/lock", 0755)
    chmod("/var/tmp", 01777)

    # FHS compatibility symlinks stuff
    pisitools.dosym("/var/tmp", "/usr/tmp")
    pisitools.dosym("share/man", "/usr/local/man")

    if get.ARCH() == "x86_64":
        # Hack for binary blobs built on multi-lib systems
        pisitools.dosym("lib", "/lib64")
