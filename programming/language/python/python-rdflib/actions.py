#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # rdfpipe does not work without egg-info files, please do not remove it!
    #pisitools.removeDir("/usr/lib/%s/site-packages/rdflib-%s-py%s.egg-info" % (get.curPYTHON(), get.srcVERSION(), get.curPYTHON().replace("python", "")))
