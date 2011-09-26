#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def install():
    pisitools.dosed("conf/config.pl", "\$Conf{CgiAdminUsers}.*= '';", "$Conf{CgiAdminUsers}     = 'admin';")
    shelltools.system("perl configure.pl \
               --batch \
               --backuppc-user=apache \
               --dest-dir %s \
               --config-dir /%s/BackupPC \
               --cgi-dir /%s/BackupPC/cgi-bin \
               --data-dir /%s/lib/BackupPC \
               --hostname localhost \
               --html-dir /%s/BackupPC/html \
               --html-dir-url /BackupPC \
               --install-dir /%s/BackupPC \
               --log-dir /%s/log/BackupPC"
              % (get.installDIR(), get.confDIR(), get.dataDIR(), get.localstateDIR(), get.dataDIR(), get.dataDIR(), get.localstateDIR()))

    pisitools.dodoc("ChangeLog", "LICENSE", "README", "doc/*")
