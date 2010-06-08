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

def setup():
    shelltools.export("gl_cv_func_printf_directive_n", "yes")
    shelltools.export("gl_cv_func_isnanl_works", "yes")
    shelltools.export("DEFAULT_POSIX2_VERSION", "199209")
    shelltools.export("AUTOPOINT", "/bin/true")

    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-largefile \
                         --enable-nls \
                         --enable-acl \
                         --enable-xattr \
                         --enable-install-program=arch \
                         --disable-libcap \
                         --without-included-regex \
                         --without-gmp \
                         --enable-no-install-program=faillog,hostname,login,lastlog,uptime")

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

# check does horrible things like modifying mtab or loop mounting
# use it if you are too curious
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use dircolors from the package
    pisitools.insinto("/etc", "src/dircolors.hin", "DIR_COLORS")

    # move critical files into /bin
    for file in ["cat","chgrp","chmod","chown","cp","date","dd","df",
                 "dir","echo","false","ln","ls","mkdir","mknod","mv",
                 "pwd","readlink","rm","rmdir","sleep","stty","sync",
                 "touch","true","uname","vdir"]:
        pisitools.domove("/usr/bin/%s" % file, "/bin/")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")

