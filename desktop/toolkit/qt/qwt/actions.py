#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()


def install():
    qt4.install()

    pisitools.doman("doc/man/*/*")
    pisitools.dohtml("doc/html/*")
    pisitools.insinto("/usr/share/doc/qwt/examples", "examples")
