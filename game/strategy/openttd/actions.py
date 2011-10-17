#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("--without-allegro \
                            --prefix-dir=/%s \
                            --binary-dir=bin \
                            --data-dir=share/openttd \
                            --install-dir=%s \
                            --doc-dir=share/doc/openttd \
                            --icon-theme-dir=share/icons/hicolor \
                            " % (get.defaultprefixDIR(),
                                get.installDIR(),
                            ))

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/%s/share/pixmaps" % get.defaultprefixDIR())
