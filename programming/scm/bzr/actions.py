#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/etc/bash_completion.d/", "contrib/bash/bzr")
    pisitools.removeDir("/usr/lib/%s/site-packages/bzrlib/util/elementtree" \
                        % get.curPYTHON())

    pisitools.dodoc("COPYING.txt", "README", "NEWS", "TODO")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "doc/*")
