#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "python-mode"

def install():
    pisitools.insinto("/usr/share/emacs/site-lisp/python", "*.el", "python-mode.el")
