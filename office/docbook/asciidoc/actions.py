# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install-vim" % get.installDIR())

    # Move data files and create symlinks for asciidoc to work
    for d in ("dblatex", "docbook-xsl", "images", "javascripts", "stylesheets"):
        pisitools.domove("/etc/asciidoc/%s" % d, "/usr/share/asciidoc")
        pisitools.dosym("/usr/share/asciidoc/%s" % d, "/etc/asciidoc/%s" % d)

    # Python module
    pisitools.insinto("/usr/lib/%s/site-packages" % get.curPYTHON(), "asciidocapi.py")

    # Vim syntax and filetype plugins
    pisitools.insinto("/usr/share/vim/vimfiles/ftdetect/" , "vim/ftdetect/asciidoc_filetype.vim", "asciidoc.vim")
    pisitools.insinto("/usr/share/vim/vimfiles/syntax/" , "vim/syntax/asciidoc.vim")

    pisitools.dodoc("BUGS", "CHANGELOG", "COPYING", "README")
    pisitools.dodoc("docbook-xsl/asciidoc-docbook-xsl.txt", "filters/code/code-filter-readme.txt")
