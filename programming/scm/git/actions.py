# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

config = """
V                       = 1
CFLAGS                  = %s
LDFLAGS                 = %s
INSTALLDIRS             = vendor
DESTDIR                 = %s
prefix                  = /usr
htmldir                 = /usr/share/doc/git
ETC_GITCONFIG           = /etc/gitconfig
GITWEB_CSS              = gitweb/gitweb.css
GITWEB_LOGO             = gitweb/git-logo.png
GITWEB_FAVICON          = gitweb/git-favicon.png
GITWEB_JS               = gitweb/gitweb.js
gitwebdir               = /var/www/localhost/cgi-bin
ASCIIDOC8               = 1
ASCIIDOC_NO_ROFF        = 1
BLK_SHA1                = 1
NEEDS_CRYPTO_WITH_SSL   = 1
NO_PYTHON               = 1
""" % (get.CFLAGS(), get.LDFLAGS(), get.installDIR())

def setup():
    shelltools.echo("config.mak", config)
    pisitools.dosed("gitweb/Makefile", "^(gitwebstaticdir_SQ = .*)static(.*)", r"\1gitweb\2")

def build():
    pisitools.dosed("Makefile", "^CC = .*$", "CC = %s" % get.CC())
    autotools.make("all doc gitweb/gitweb.cgi")

def install():
    autotools.rawInstall("install-doc")

    # Install bash completion
    pisitools.insinto("/etc/bash_completion.d", "contrib/completion/git-completion.bash", "git")
    shelltools.chmod("%s/etc/bash_completion.d/git" % get.installDIR(), 0644)

    # for git-daemon
    pisitools.dodir("/pub/scm")

    # Remove useless perl directories
    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())
    pisitools.removeDir("/usr/lib/perl5/site_perl/%s/%s-linux-thread-multi" % (get.curPERL(), get.ARCH()))

    # Some docs
    pisitools.dodoc("README", "COPYING", "Documentation/SubmittingPatches")
