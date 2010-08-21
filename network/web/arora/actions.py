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

WorkDir="arora-0.10.2"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "LICENSE*")
