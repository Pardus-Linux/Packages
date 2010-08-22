#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = 'qca-%s' % (get.srcVERSION())

def setup():
    autotools.rawConfigure("--prefix=/%s --datadir=/usr/share --no-separate-debug-info --verbose" % get.defaultprefixDIR())

def build():
    autotools.make()
    autotools.make("apidox")

def install():
    # Remove source build directory variable
    pisitools.dosed("lib/libqca.prl", "^QMAKE_PRL_BUILD_DIR.*$")

    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Put apidocs in its own directory
    pisitools.dodir("/usr/share/doc/qca2-apidocs/html")
    pisitools.insinto("/usr/share/doc/qca2-apidocs/html", "apidocs/html/*")

    # Create symlink for qcatool
    #pisitools.dosym("/usr/qt/4/bin/qcatool2", "/usr/bin/qcatool2")

    #Use openssl CA list instead of the outdated QCA root CA list
    #pisitools.remove("/usr/share/qca/certs/rootcerts.pem")
    #pisitools.dosym("/etc/ssl/certs/ca-bundle.crt", "/usr/share/qca/certs/rootcerts.pem")

    pisitools.dodoc("README", "TODO", "COPYING")
