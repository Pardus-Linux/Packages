#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="krb5-%s" % get.srcVERSION()

def rename_man_pages():
    manpages = ["appl/bsd/klogind.M",
                "appl/bsd/kshd.M",
                "appl/sample/sserver/sserver.M",
                "appl/telnet/telnetd/telnetd.8",
                "appl/gssftp/ftpd/ftpd.M",
                "config-files/kdc.conf.M",
                "config-files/krb5.conf.M",
                "kadmin/cli/kadmin.M",
                "slave/kpropd.M",
                "slave/kprop.M"]
    for manpage in manpages:
        shelltools.move(manpage, "%s.in" % manpage)

def setup():
    shelltools.cd("src")

    # Rebuild configure scripts
    shelltools.chmod("rebuild-configure-scripts.sh")
    shelltools.system("./rebuild-configure-scripts.sh")

    # Rename man pages to regenerate them
    rename_man_pages()

    shelltools.export("CFLAGS", "-I/usr/include/et -fPIC -fno-strict-aliasing %s" % get.CFLAGS())

    # Fix pthread linking
    pisitools.dosed("configure", "-lthread", "-lpthread")
    pisitools.dosed("configure", "-pthread", "-lpthread")

    autotools.configure("--with-system-et \
                         --with-system-ss \
                         --with-pam \
                         --with-ldap \
                         --with-netlib=-lresolv \
                         --without-selinux \
                         --without-tcl \
                         --localstatedir=/var/lib/kerberos \
                         --disable-rpath \
                         --enable-shared \
                         --enable-pkinit \
                         --enable-dns \
                         --enable-dns-for-realm")

    # Fix krb5-config script to remove rpaths and CFLAGS
    pisitools.dosed("krb5-config", "^CC_LINK=.*", "CC_LINK='$(CC) $(PROG_LIBPATH)'")

def build():
    autotools.make("-C src/")

def check():
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp(prefix='pisitest')
    autotools.make("-C src/ check TMPDIR=%s -j1" % tmpdir)
    shutil.rmtree("rm -rf %s" % tmpdir)

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install additional headers
    for d in ("kadm5", "krb5"):
        pisitools.insinto("/usr/include/%s" % d, "include/%s/*.h" % d)

    # Add "k" prefix to some apps and manpages to resolve conflicts
    for app in ["telnetd", "ftpd"]:
        pisitools.rename("/usr/share/man/man8/%s.8" % app, "k%s.8" % app)
        pisitools.rename("/usr/sbin/%s" % app, "k%s" % app)

    for app in ["rcp", "rsh", "telnet", "ftp", "rlogin"]:
        pisitools.rename("/usr/share/man/man1/%s.1" % app, "k%s.1" % app)
        pisitools.rename("/usr/bin/%s" % app, "k%s" % app)

    # Install info and docs
    pisitools.doinfo("../doc/*.info")
    pisitools.dodoc("../README")

    # Remove examples
    pisitools.removeDir("/usr/share/examples")
