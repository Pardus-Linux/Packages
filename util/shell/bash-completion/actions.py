#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

import os

def setup():
    autotools.configure()

def build():
    autotools.make("bash_completion.sh")

def install():
    pisitools.insinto("/etc", "bash_completion")

    pisitools.insinto("/usr/share/bash-completion", "contrib/*")

    blacklist = ["mplayer", "mount"]
    for comp in blacklist:
        pisitools.remove("/usr/share/bash-completion/%s" % comp)

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README", "TODO")
