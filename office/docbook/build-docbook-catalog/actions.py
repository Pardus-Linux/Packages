#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pisitools.dobin("build-docbook-catalog-%s" % get.srcVERSION())

    pisitools.domove("/usr/bin/build-docbook-catalog-%s" % get.srcVERSION(), "/usr/bin", "build-docbook-catalog")
