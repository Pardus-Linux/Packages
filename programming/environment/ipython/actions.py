#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.removeDir("/usr/share/doc/ipython")

    pisitools.dodir("/usr/share/emacs/site-lisp")
    pisitools.insinto("/usr/share/emacs/site-lisp", "docs/emacs/ipython.el")

    pisitools.dodoc("README.txt")
