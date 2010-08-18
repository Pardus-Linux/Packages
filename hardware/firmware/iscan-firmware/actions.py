#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import glob

WorkDir="iscan-firmwares-%s" % get.srcVERSION()

def install():

    # Get plugins list
    plugins = shelltools.ls(".")

    # Install the firmware files
    for pl in plugins:
        files = shelltools.ls("%s/usr/share/iscan" % pl)
        if len(files) > 0:
            pisitools.insinto("/usr/share/iscan", "%s/usr/share/iscan/%s" % (pl, files[0]))

    # Install the libraries
    libs = [f.rpartition(get.curDIR()+'/')[-1] for f in glob.glob("%s/*/usr/lib/iscan/*" % get.curDIR())
                    if not shelltools.isLink(f)]

    for l in libs:
        pisitools.dolib_so(l, "/usr/lib/iscan")
        pisitools.dosym(shelltools.baseName(l), "/%s" % l.split("/", 1)[1].split(".")[0]+'.so')
        pisitools.dosym(shelltools.baseName(l), "/%s" % l.split("/", 1)[1].split(".")[0]+'.so.2')

    # Dodoc one of the plugins doc files, it's all same.
    for d in shelltools.ls("iscan-plugin-gt-f520/usr/share/doc/iscan-plugin-gt-f520-1.0.0"):
        pisitools.dodoc("iscan-plugin-gt-f520/usr/share/doc/iscan-plugin-gt-f520-1.0.0/%s" % d)



