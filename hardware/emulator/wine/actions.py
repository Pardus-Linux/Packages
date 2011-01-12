# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "wine-%s" % get.srcVERSION().replace("_", "-")

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--without-capi \
                         --with-curses \
                         --without-esd \
                         --with-opengl \
                         --with-pulse")

def build():
    autotools.make()

def install():
    autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true")

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
