#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = get.ARCH()
NoStrip = "/"
Name = "6u22"
Arch = "amd64" if get.ARCH() == "x86_64" else "i586"

def setup():
    shelltools.system("sh jdk-%s-dlj-linux-%s.bin --accept-license" % (Name, Arch))

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct . %s/opt/sun-jdk %s/opt/sun-jre"% (get.installDIR(),get.installDIR()))

    pisitools.dodir("/usr/lib/browser-plugins")

    # Next generation Java plugin is needed by Firefox 3.6+
    # http://java.sun.com/javase/6/webnotes/install/jre/manual-plugin-install-linux.html
    pisitools.dosym("/opt/sun-jre/lib/%s/libnpjp2.so" % Arch.replace("i586", "i386"), "/usr/lib/browser-plugins/javaplugin.so")

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "README_ja.html", "README_zh_CN.html", "THIRDPARTYLICENSEREADME.txt"]:
        file = "%s/opt/sun-jdk/%s" % (get.installDIR(), doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)
