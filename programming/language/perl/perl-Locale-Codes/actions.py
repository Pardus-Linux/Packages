#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    #This files are included in Perl 5.12.1
    for locale in ["Currency", "Constants", "Country" , "Script", "Language"]:
        pisitools.remove("/usr/share/man/man3/Locale::%s.3pm" % locale)
        pisitools.remove("/usr/lib/perl5/vendor_perl/%s/Locale/%s.pm" % (get.curPERL(), locale))

    pisitools.dodoc("README")

