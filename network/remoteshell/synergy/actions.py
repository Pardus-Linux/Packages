#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = 'synergy-plus-1.3.4'

def setup():
    autotools.autoreconf('-fi')
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto('/etc','examples/synergy.conf')
    shelltools.chmod('%s/etc/synergy.conf' % get.installDIR(), 0644)

    pisitools.dodoc('ChangeLog','COPYING','NEWS','README')
