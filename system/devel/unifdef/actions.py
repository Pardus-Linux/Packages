#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin("unifdef")
    pisitools.dobin("unifdefall.sh")

    pisitools.doman("unifdef.1")
