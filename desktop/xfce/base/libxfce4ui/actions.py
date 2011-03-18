#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system('xdt-autogen')
    autotools.configure('--enable-startup-notification')

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())
    pisitools.dodoc('NEWS', 'COPYING', 'README', 'TODO', 'ChangeLog', 'AUTHORS', 'THANKS')
