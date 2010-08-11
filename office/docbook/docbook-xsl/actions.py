#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s/usr/share/sgml/docbook/xsl-stylesheets"
                         % get.installDIR())

    # Don't ship the extensions
    pisitools.remove("/usr/share/sgml/docbook/xsl-stylesheets/extensions/*")

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README", "RELEASE-NOTES.txt", "TODO", "VERSION")
