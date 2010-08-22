#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="%s" % get.srcNAME().replace("perl-", "")

def install():
    pisitools.chmod("*",0644)
    pisitools.chmod("sgmlspl.pl")

    vendordir = "/usr/lib/perl5/vendor_perl/%s" % get.curPERL()
    pisitools.dodir(vendordir)
    pisitools.dodir("/usr/bin")

    autotools.make("install_system BINDIR=%s/usr/bin PERL5DIR=%s/%s" % (get.installDIR(), get.installDIR(), vendordir))

    pisitools.dodoc("ChangeLog","README","COPYING")
