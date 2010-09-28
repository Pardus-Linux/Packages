#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

#WorkDir="PyQt-x11-gpl-%s" % get.srcVERSION()
WorkDir="PyQt-x11-gpl-snapshot-4.8-eac5dd92c907"

def setup():
    pisitools.dosed("configure.py", "  check_license()", "# check_license()")
    pythonmodules.run("configure.py -q /usr/bin/qmake")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})

    pisitools.dohtml("doc/html/*")
    pisitools.dosym("/usr/share/doc/%s/html/classes.html" % get.srcNAME(),"/usr/share/doc/%s/html/index.html" % get.srcNAME())

    pisitools.dodoc("NEWS", "README", "THANKS", "LICENSE*", "GPL*", "OPENSOURCE*")

