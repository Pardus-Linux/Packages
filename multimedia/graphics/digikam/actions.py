#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright TUBITAK
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
shelltools.export("HOME", get.workDIR())

def setup():
    # This docbook is buggy
    # pisitools.dosed("doc-translations/CMakeLists.txt", "^(add_subdirectory\( pt_digikam/digikam \))$", "#\\1")

    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    """
    for d in ["sv"]:
        pisitools.remove("/usr/share/kde4/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
        pisitools.dosym("/usr/share/kde4/doc/HTML/en/common", "/usr/share/kde4/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
    """

    pisitools.dodoc("README", "COPYING*", "AUTHORS", "NEWS")
