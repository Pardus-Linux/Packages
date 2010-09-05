#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "python-%s-docs-html" % get.srcVERSION()
docdir = "/%s/%s/html" % (get.docDIR(), get.srcNAME())

def install():
    pisitools.insinto(docdir, "*")
    pisitools.removeDir("%s/_sources" % docdir)

    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50python-docs" % get.installDIR(), "PYTHONDOCS=%s/library" % docdir)

