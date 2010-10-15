#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcNAME()))

    pisitools.copytree("Oxygen-Air", "%s/usr/share/smplayer/themes/Oxygen-Air" % get.installDIR())
