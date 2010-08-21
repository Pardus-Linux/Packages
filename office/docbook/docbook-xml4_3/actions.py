#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def install():
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s" % get.srcVERSION(), "*.dtd")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s" % get.srcVERSION(), "*.mod")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s" % get.srcVERSION(), "docbook.cat")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s/ent" % get.srcVERSION(), "ent/*.ent")

    pisitools.dodoc("ChangeLog", "README")

