# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

demos_dir = "/usr/lib/mesa/demos"

def setup():
    autotools.configure("--bindir=%s \
                         --disable-static" % demos_dir)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for util in ("glxgears", "glxinfo"):
        pisitools.domove("%s/%s" % (demos_dir, util), "/usr/bin/")
