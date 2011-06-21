#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = 'synergy-1.4.2-Source'

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    pisitools.dobin('synergyc')
    pisitools.dobin('synergys')

    shelltools.chmod('%s/conf/synergy.conf' % get.curDIR(), 0644)
    pisitools.insinto('/etc','conf/synergy.conf')

    pisitools.dodoc('ChangeLog', 'COPYING', 'README')
