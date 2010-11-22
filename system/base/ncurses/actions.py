#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ncurses-%s" % get.srcVERSION().split("_", 1)[0]
multilib = (get.ARCH() == "x86_64")

configparams = "--without-debug \
               --without-profile \
               --disable-rpath \
               --enable-const \
               --enable-largefile \
               --enable-widec \
               --with-terminfo-dirs='/etc/terminfo:/usr/share/terminfo' \
               --disable-termcap \
               --with-shared \
               --with-rcs-ids \
               --with-chtype='long' \
               --with-mmask-t='long' \
               --without-ada \
               --enable-symlinks"


def linknonwide(targetDir):
    # symlink normal objects to widechar ones, to force widechar enabling
    for f in shelltools.ls("%s/%s/*w.*" % (get.installDIR(), targetDir)):
        source = shelltools.baseName(f)
        destination = source.replace("w.", ".")
        pisitools.dosym(source, "%s/%s" % (targetDir, destination))

def setup():
    autotools.configure(configparams)

    if multilib:
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.makedirs("build32")
        shelltools.cd("build32")
        shelltools.system("../configure %s --without-gpm" % configparams)

def build():
    autotools.make()

    if multilib:
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.cd("build32")
        autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Handle static libs in /usr/%libdir/static
    pisitools.dodir("/usr/lib/static")
    for i in shelltools.ls("%s/usr/lib/*.a" % get.installDIR()):
        pisitools.domove("/usr/lib/%s" % shelltools.baseName(i), "/usr/lib/static/")

    linknonwide("/usr/lib/static")
    linknonwide("/usr/lib")

    if multilib:
        pisitools.dodir("/usr/lib32/static")
        for i in shelltools.ls("build32/lib/*.a"):
            pisitools.insinto("/usr/lib32/static/", "build32/lib/%s" % shelltools.baseName(i))

        linknonwide("/usr/lib32/static")


    # We need the basic terminfo files in /etc
    terminfo = ["ansi", "console", "dumb", "linux", "rxvt", "screen", "sun", \
                "vt52", "vt100", "vt102", "vt200", "vt220", "xterm", "xterm-color", "xterm-xfree86"]

    for f in terminfo:
        termfile = f[0] + "/" + f
        if shelltools.can_access_file("/usr/share/terminfo/%s" % termfile):
            pisitools.dodir("/etc/terminfo/%s" % f[0])
            pisitools.domove("/usr/share/terminfo/%s" % termfile, "/etc/terminfo/%s" % f[0])
            pisitools.dosym("../../../../etc/terminfo/%s/%s" % (f[0], f), "/usr/share/terminfo/%s/%s" % (f[0], f))

    pisitools.dodoc("ANNOUNCE", "NEWS", "README*", "TO-DO")

