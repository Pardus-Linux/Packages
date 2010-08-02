#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "glibc-2.12-26-g9a98163"

defaultflags = "-O3 -U_FORTIFY_SOURCE -fno-strict-aliasing -mno-tls-direct-seg-refs"
sysflags = get.CFLAGS().replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "")
buildflags = "%s %s" % (sysflags, defaultflags)


def set_variables():
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    # shelltools.export("CC", "gcc")
    # shelltools.export("CXX", "g++")

    shelltools.export("CFLAGS", buildflags)
    shelltools.export("CXXFLAGS", buildflags)

def setup():
    set_variables()

    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure \
                       --with-tls \
                       --with-__thread \
                       --enable-add-ons=nptl,libidn \
                       --enable-bind-now \
                       --enable-kernel=2.6.31 \
                       --enable-stackguard-randomization \
                       --without-cvs \
                       --without-gd \
                       --without-selinux \
                       --build=%s \
                       --host=%s \
                       --disable-profile \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --libexecdir=/usr/lib/misc" % (get.HOST(), get.HOST()))

def build():
    set_variables()

    shelltools.cd("build")
    autotools.make()

# FIXME: yes fix me
#def check():
#    set_variables()
#    shelltools.chmod("scripts/begin-end-check.pl")
#
#    shelltools.cd("build")
#
#    shelltools.export("TIMEOUTFACTOR", "16")
#    autotools.make("-k check 2>error.log")

def install():
    # These should not be set, else the zoneinfo do not always get installed ...
    set_variables()

    # install glibc/glibc-locale files
    shelltools.cd("build")
    autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

    # Some things want this, notably ash
    pisitools.dosym("libbsd-compat.a", "/usr/lib/libbsd.a")

    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        pisitools.remove("/etc/ld.so.cache")

    # It previously has 0755 perms which was killing things
    shelltools.chmod("%s/usr/lib/misc/pt_chown" % get.installDIR(), 04711)

    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    shelltools.cd("..")

    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "FAQ", "NEWS", "NOTES", "PROJECTS", "README*", "LICENSES")

    # remove zoneinfo files since they are coming from timezone packages
    pisitools.removeDir("/usr/share/zoneinfo")

    for i in ["zdump", "zic"]:
        pisitools.remove("/usr/sbin/%s" % i)

