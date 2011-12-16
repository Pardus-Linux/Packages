#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--datadir=/usr/share/misc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for dic in ("connectives", "web2", "web2a", "propernames"):
        pisitools.domove("/usr/share/misc/%s" % dic, "/usr/share/dict")

    pisitools.dosym("web2", "/usr/share/dict/words")
    pisitools.dosym("web2a", "/usr/share/dict/extra.words")

    pisitools.dodoc("GNU*", "NEWS", "ORIGIN", "README", "dict-README")
