#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "acpica-unix-%s" % get.srcVERSION().split('_')[-1]

def build():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    pisitools.dosed("tools/acpiexec/Makefile", "CFLAGS\+= -Wall -g", "CFLAGS+= -Wall")

    for i in ["tools/acpisrc", "tools/acpixtract", "tools/acpiexec", "compiler/ clean", "compiler/"]:
        autotools.make("-C %s" % i)


def install():
    pisitools.dobin("compiler/iasl")

    for i in ["acpisrc", "acpiexec", "acpixtract"]:
        pisitools.dosbin("tools/%s/%s" % (i, i))

    pisitools.dodoc("changes.txt", "README")

