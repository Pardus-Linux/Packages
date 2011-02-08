#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "eric4-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/lib/%s/site-packages/eric4/i18n" % get.curPYTHON(), "eric/i18n/eric4_de.qm")
    pisitools.dodoc("README*")
