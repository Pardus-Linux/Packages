#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("ChangeLog", "README", "THANKS")

    pythonmodules.fixCompiledPy("/usr/share/kde4/apps/frescobaldi/lib/frescobaldi_app") 
    pythonmodules.fixCompiledPy("/usr/share/kde4/apps/frescobaldi/lib")
