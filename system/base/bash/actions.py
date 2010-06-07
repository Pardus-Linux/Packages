#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoconf()
    autotools.configure("--without-installed-readline \
                         --disable-profiling \
                         --without-gnu-malloc \
                         --with-curses")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domove("/usr/bin/bash", "/bin")
    pisitools.dosym("/bin/bash","/bin/sh")
    pisitools.dosym("/bin/bash","/bin/rbash")

    # Compatibility with old skels
    # pisitools.dosym("/etc/bash/bashrc", "/etc/bashrc")

    pisitools.dosym("bash.info", "/usr/share/info/bashref.info")
    pisitools.doman("doc/bash.1", "doc/bashbug.1", "doc/builtins.1", "doc/rbash.1")
    pisitools.dodoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
