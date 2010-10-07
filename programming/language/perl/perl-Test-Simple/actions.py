#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Test-Simple-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("README", "TODO", "Changes")

    # these man pages conflicts with the perl-doc package
    for manpage in ["Simple", "Builder::Tester", "Builder::Tester::Color", "Builder::Module", "More", "Tutorial", "Builder"]:
        pisitools.remove("/usr/share/man/man3/Test::%s.3pm" % manpage )
