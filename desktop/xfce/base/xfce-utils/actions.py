#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --with-terminal=Terminal \
                         --with-vendor-info=Pardus")

# Midori is still not in Pardus 2011 repositories.
# Don't forget to enable again after Midori is ready.
# --with-browser=midori \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # X config files are already in pardus-default-settings-xfce
    #pisitools.remove("/etc/xdg/xfce4/*.xrdb")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "TODO")
