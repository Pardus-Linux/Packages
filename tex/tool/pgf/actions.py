# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    for dir in ["generic", "latex", "plain", "context"]:
        pisitools.insinto("/usr/share/texmf-dist/tex/", dir)

    shelltools.cd("doc/generic/pgf")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "licenses/LICENSE", "pgfmanual.pdf")
