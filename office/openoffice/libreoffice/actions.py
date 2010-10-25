#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import re

WorkDir = "%s-build-%s" % (get.srcNAME(), get.srcVERSION())
AppDir = "/opt/LibreOffice"

# NoStrip variable will also be extended in setup method because, we need some version sstrings from configure.in file which will be used in NoStrip directories.
NoStrip = []

def baseVersion():
    return re.search("^OOO_MAJOR=(.*)$", open("%s/%s/configure.in" % (get.workDIR(), WorkDir)).read(), re.M).group(1)

def getJobCount():
    # If jobs field in pisi.conf is greater than 1, use 'this value - 1' as number of cpus. There is also a max-jobs configure opt. but it's buggy now
    return max(int(get.makeJOBS().strip().replace("-j", "")) - 1, 1)

def setup():
    NoStrip.extend(["%s/lib/ooo-%s/basis%s/share" % (AppDir, baseVersion(), baseVersion()), "%s/lib/ooo-%s/share" % (AppDir, baseVersion())])
    shelltools.export("LDFLAGS", "")

    #libdir is needed to set exec_prefix stuff of patches/dev300/system-python-ure-bootstrap.diff
    shelltools.system('./configure \
                       --prefix=%s \
                       --libdir=%s/lib \
                       --sysconfdir=/etc \
                       --with-lang="de en-US es fr hu it nl pt-BR sv tr" \
                       --disable-post-install-scripts \
                       --enable-gtk \
                       --enable-kde4 \
                       --disable-kde \
                       --enable-cairo \
                       --disable-mono \
                       --with-distro=Pardus2009 \
                       --with-drink="Burdur shish" \
                       --without-git \
                       --with-gcc-speedup=ccache \
                       --with-ant-home=/usr/share/ant \
                       --with-binsuffix=no \
                       --with-system-mdbtools \
                       --with-openclipart=/usr/share/clipart/openclipart \
                       --with-num-cpus=%s' % (AppDir, AppDir, getJobCount()))

def build():
    shelltools.export("HOME", get.workDIR())

    #temporary workaround for configure: error: unrecognized option: `-Wl,--hash-style=gnu'
    shelltools.export("LDFLAGS", "")

    autotools.make("-j1")

def install():
    shelltools.export("HOME", get.workDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #dosym main executables
    for bin in map(os.path.basename, shelltools.ls("%s/%s/bin/oo*" % (get.installDIR(), AppDir))):
        pisitools.dosym("%s/bin/%s" % (AppDir, bin), "/usr/bin/%s" % bin)

    #make symlink of unopkg
    pisitools.dosym("%s/bin/unopkg" % AppDir,"/usr/bin/unopkg")

    # Icons
    pisitools.insinto("/usr/share/pixmaps","desktop/48x48/*.png")

    # Icon symlinks
    pisitools.dosym("/usr/share/pixmaps/ooo-impress.png","/usr/share/pixmaps/presentation.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-writer.png","/usr/share/pixmaps/wordprocessing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-calc.png","/usr/share/pixmaps/spreadsheet.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-base.png","/usr/share/pixmaps/database.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-draw.png","/usr/share/pixmaps/drawing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-math.png","/usr/share/pixmaps/formula.png")

    #Put pyuno to python directory and add python modules directory to sys.path in uno.py
    unoPath = "%s/lib/ooo-%s/basis%s/program/uno.py" % (AppDir, baseVersion(), baseVersion())
    unopy = open(get.installDIR() + unoPath).read()
    pisitools.dodir("/usr/lib/%s/site-packages/" % get.curPYTHON())
    newunopy = open("%s/usr/lib/%s/site-packages/uno.py" % (get.installDIR(), get.curPYTHON()), "w")
    newunopy.write("import sys\nsys.path.append('%s/lib/ooo-%s/basis%s/program')\n%s" % (AppDir, baseVersion(), baseVersion(), unopy))
    newunopy.close()
    pisitools.remove(unoPath)
    pisitools.domove("%s/lib/ooo-%s/basis%s/program/unohelper.py" % (AppDir, baseVersion(), baseVersion()), "/usr/lib/%s/site-packages" % get.curPYTHON())

    #install man files
    pisitools.domove("%s/share/man/man1/*" % AppDir, "/usr/share/man/man1")
    pisitools.removeDir("%s/share/man" % AppDir)

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")

    #TODO do we need those workarounds?
    #Workaround for #11530, bnc#502641
    #pisitools.dosed("%s/%s/lib/ooo-%s/basis%s/share/registry/data/org/openoffice/Office/Calc.xcu" % (get.installDIR(), AppDir, baseVersion(), baseVersion()), "</oor:component-data>", " <node oor:name=\"Formula\">\n  <node oor:name=\"Syntax\">\n   <prop oor:name=\"Grammar\" oor:type=\"xs:int\">\n    <value>0</value>\n   </prop>\n  </node>\n </node>\n</oor:component-data>")

    plastikWorkaround="""qtWidgetStyle=`kreadconfig --file kdeglobals --group General --key widgetStyle`
if test "x$qtWidgetStyle" != xqtcurve -a "x$qtWidgetStyle" != xoxygen ;
then
export OOO_FORCE_DESKTOP=gnome
fi
"""
    #Fallback to GTK/GNOME UI if a widget style other than oxygen/qtcurve is preferred #13281
    #pisitools.dosed("%s/%s/lib/ooo-%s/program/soffice" % (get.installDIR(), AppDir, baseVersion()), "export SAL_ENABLE_FILE_LOCKING", "export SAL_ENABLE_FILE_LOCKING\n%s\n" % plastikWorkaround)

    #install our own sofficerc file
    #pisitools.insinto("%s/lib/ooo-%s/program" % (AppDir, baseVersion()), "sofficerc.pardus", "sofficerc")
