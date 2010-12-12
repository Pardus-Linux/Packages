#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pisitools.dosed("cherrypy/test/test.py", "raw_input", "")
    pisitools.dosed("cherrypy/test/test.py", "'test_cache_filter',", "")

    pythonmodules.install()

    pisitools.dodoc("README.txt", "CHANGELOG.txt", "CHERRYPYTEAM.txt")
