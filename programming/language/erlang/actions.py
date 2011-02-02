#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="otp_src_R14B"

def setup():
    autotools.configure("--enable-threads \
                         --with-ssl")

def build():
    autotools.make("-j1")

def install():
    join = os.path.join
    install_dir = get.installDIR()
    work_dir = get.workDIR()
    erl_dir = join(install_dir, "/usr/lib/erlang")

    autotools.install()

    # fix paths
    for root, dirs, files in os.walk(install_dir):
        for f in files:
            if f.endswith(".beam"):
                continue
            f = join(root, f)
            pisitools.dosed(f, install_dir, "")

    # remove no longer needed file
    pisitools.remove("/usr/lib/erlang/Install")

    # Emacs erlang-mode
    erl_emacs_dir = join(work_dir, WorkDir, "lib/tools/emacs")
    pisitools.insinto("/usr/share/emacs/site-lisp/erlang", erl_emacs_dir + "/*.el")
