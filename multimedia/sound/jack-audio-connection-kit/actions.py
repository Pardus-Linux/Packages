#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir = "jack-%s" % get.srcVERSION()
del(os.environ["JOBS"])

def setup():
    shelltools.system("./waf configure \
                        --prefix=/usr \
                        --doxygen \
                        --dbus \
                        --classic")

def build():
    shelltools.system("./waf build -v")

def install():
    shelltools.system("./waf --destdir=%s install" % get.installDIR())

    # be compatible with the former jackaudio
    pisitools.rename("/usr/bin/jack_rec", "jackrec")

    shelltools.chmod("%s/usr/lib/jack/*.so*" % get.installDIR(), 0755)

    pisitools.dodoc("ChangeLog", "README*", "TODO")
