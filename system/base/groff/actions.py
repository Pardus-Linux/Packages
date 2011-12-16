#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-appresdir=/usr/share/X11/app-defaults \
                         --without-gs \
                         --disable-rpath \
                         --without-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # required by man
    for file_ in ("gnroff", "gtroff", "gtbl", "gpic", "geqn", "gneqn",
                  "grefer", "glookbib", "gindxbib", "gsoelim", "zsoelim"):
        pisitools.dosym(file_[1:], "/usr/bin/%s" % file_)
        pisitools.dosym(file_[1:], "/usr/share/man/man1/%s.1" % file_)

    pisitools.removeDir("/usr/share/doc/*-%s" % get.srcVERSION())

    pisitools.dodoc("ChangeLog", "NEWS", "PROBLEMS", "PROJECTS", "README")
