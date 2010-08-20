#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "vim73"

def setup():
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    shelltools.export("CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    pisitools.dosed("runtime/tools/mve.awk", "#!/usr/bin/nawk -f", "#!/usr/bin/awk -f")

    shelltools.echo("src/feature.h", "#define SYS_VIMRC_FILE \"/etc/vim/vimrc\"")

    pisitools.dosed("runtime/doc/syntax.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/tagsrch.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/usr_29.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/menu.vim", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("src/configure.in", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")

    pisitools.dosed("src/configure.in", "libc.h", "")
    pisitools.dosed("src/Makefile", " auto.config.mk:", ":")

    autotools.make("-C src autoconf")

    #fix sun-jdk sandbox error
    shelltools.export("MANPATH", "/usr/share/man")

    configure_args="--with-features=huge \
                    --enable-multibyte \
                    --enable-perlinterp \
                    --enable-pythoninterp \
                    --with-tlib=ncurses \
                    --disable-acl \
                    --with-compiledby=http://bugs.pardus.org.tr \
                    --with-modified-by=http://bugs.pardus.org.tr"

    shelltools.copytree("%s/vim73" % get.workDIR(),"build-gui")

    autotools.configure("%s\
                         --enable-gui=no" % configure_args)

    # Build gui
    shelltools.cd("build-gui")
    autotools.configure("%s\
                         --with-vim-name=vim-gtk \
                         --enable-gui=yes \
                         --with-x" % configure_args)
def build():
    autotools.make("-C src/")

    autotools.make("-C build-gui/src/")

def install():
    dirs = ['/usr/bin', '/etc/vim', '/usr/share', '/usr/share/man', '/usr/share/vim']
    for a in dirs:
        pisitools.dodir(a)

    install_args="DESTDIR=%s \
                  BINDIR=/usr/bin \
                  MANDIR=/usr/share/man \
                  DATADIR=/usr/share" % get.installDIR()

    autotools.rawInstall("-C src/  %s \
                                   installruntime \
                                   installmacros \
                                   installtutor \
                                   installtools \
                                   install-languages \
                                   install-icons" % install_args)

    autotools.rawInstall("-C build-gui/src %s" % install_args, "installvimbin")

    pisitools.dosym("vim", "/usr/bin/vi")
    pisitools.dosym("/usr/bin/vim", "/bin/ex")

    pisitools.rename("/usr/bin/vim-gtk", "gvim")

    for link in ("evim", "eview", "gview", "gvimdiff", "rgview", "rgvim"):
        pisitools.dosym("gvim", "/usr/bin/%s" % link)
