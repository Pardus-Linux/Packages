#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

def setup():
    # Respect the user LDFLAGS
    shelltools.system("./autogen.sh")

    shelltools.export("EXTRA_LDFLAGS", get.LDFLAGS())

    autotools.configure("--disable-static \
                         --with-jdk=/opt/sun-jdk/ \
                         --enable-javahl \
                         --with-neon=/usr \
                         --with-apr=/usr \
                         --with-apr-util=/usr \
                         --with-apxs=/usr/sbin/apxs \
                         --with-zlib=/usr \
                         --with-jikes=no \
                         --disable-mod-activation")

def build():
    # svn
    autotools.make()

    # python bindings
    autotools.make("swig-py")

    # perl bindings (needed by git-svn*)
    autotools.make("swig-pl")

    # java bindings
    autotools.make("-j1 javahl")

def install():
    # install svn
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install swig-py
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-swig-py")

    # install swig-pl
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-swig-pl")

    # install javahl
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-javahl")

    # Move py/c'into proper dir
    pisitools.domove("/usr/lib/svn-python/svn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/svn-python/libsvn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.removeDir("/usr/lib/svn-python")

    # some helper tools
    pisitools.insinto("/usr/bin", "tools/backup/hot-backup.py", "svn-hot-backup")
    # FIXME: these tools are replaced by new ones
    # pisitools.insinto("/usr/bin", "contrib/client-side/svn_load_dirs.pl", "svn-load-dirs")
    # pisitools.insinto("/usr/bin", "contrib/client-side/svnmerge.py", "svnmerge")
    # shelltools.chmod("%s/usr/bin/svnmerge" % get.installDIR(), 0755)

    # remove useless .packlist by hand.
    pisitools.remove("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/auto/SVN/_Core/.packlist" % (get.curPERL(), get.ARCH()))

    # Documentation and etc.
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "contrib")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "tools/xslt")
    pisitools.insinto("/var/www/localhost/htdocs", "tools/xslt/*")
    pisitools.dodoc("COPYING", "README")
