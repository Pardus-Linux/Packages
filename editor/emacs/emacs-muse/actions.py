#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" %get.installDIR())

    pisitools.remove("/usr/share/emacs/site-lisp/muse/*.elc")
    pisitools.remove("/usr/share/emacs/site-lisp/muse/contrib/*.elc")

    pisitools.doinfo("texi/*.info")
    pisitools.dodoc("COPYING", "AUTHORS", "NEWS", "README")
