#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


cfgsettings = """-DDEFAULT_PATH_VALUE=\'\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"\' \
                 -DSTANDARD_UTILS_PATH=\'\"/bin:/usr/bin:/sbin:/usr/sbin\"\' \
                 -DSYS_BASHRC=\'\"/etc/bash/bashrc\"\' \
                 -DNON_INTERACTIVE_LOGIN_SHELLS \
                 -DSSH_SOURCE_BASHRC"""

def setup():
    # Recycles pids is neccessary. When bash's last fork's pid was X and new fork's pid is also X,
    # bash has to wait for this same pid. Without Recycles pids bash will not wait.
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE -DRECYCLES_PIDS %s " % (get.CFLAGS(), cfgsettings))

    autotools.autoconf()
    autotools.configure("--with-bash-malloc=no \
                         --disable-rpath")

def build():
    autotools.make()

# FIXME: package build stops right after checking even when no errors happen (probably
# due to SIGHUP in test). It is the duty of the packager to run tests by hand.
#def check():
#    autotools.make("check")

def install():
    autotools.install()

    pisitools.dosym("/usr/bin/bash","/bin/sh")
    pisitools.dosym("/usr/bin/bash","/bin/rbash")
    pisitools.dosym("/usr/bin/bash","/bin/bash")

    pisitools.dosym("bash.info", "/usr/share/info/bashref.info")
    pisitools.doman("doc/bash.1", "doc/bashbug.1", "doc/builtins.1", "doc/rbash.1")
    pisitools.dodoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
