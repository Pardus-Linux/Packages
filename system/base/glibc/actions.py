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

import os

WorkDir = "glibc-2.12-26-g9a98163"

defaultflags = "-O3 -U_FORTIFY_SOURCE -fno-strict-aliasing -mno-tls-direct-seg-refs"
sysflags = get.CFLAGS().replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "").replace("-funwind-tables", "").replace("-fasynchronous-unwind-tables", "")

multibuild = (get.ARCH() == "x86_64")
pkgworkdir = "%s/%s" % (get.workDIR(), WorkDir)

config = {"multiarch": {
                "multi": True,
                "extraconfig": "--build=i686-pc-linux-gnu --enable-multi-arch",
                "coreflags":   "-m32",
                "libdir":      "lib32",
                "buildflags":  "-mtune=atom -march=i686 -O2 -pipe -fomit-frame-pointer %s" % defaultflags,
                "builddir":    "%s/build32" % pkgworkdir
            },
           "system": {
                "multi": False,
                "extraconfig": "--build=%s" % get.HOST(),
                "coreflags":   "",
                "libdir":      "lib",
                "buildflags":  "%s %s" % (sysflags, defaultflags),
                "builddir":    "%s/build" % pkgworkdir
            }
}

ldconf32bit = """/lib32
/usr/lib32
"""
#/usr/local/lib32


### helper functions ###
def removePardusSection(_dir):
    for k in shelltools.ls(_dir):
        # FIXME: should we do this only on nonshared or all ?
        # if ("crt" in k and k.endswith(".o")) or k.endswith("nonshared.a"):
        if ("crt" in k and k.endswith(".o")) or k.endswith(".a"):
            i = os.path.join(_dir, k)
            shelltools.system('objcopy -R ".comment.PARDUS.OPTs" -R ".note.gnu.build-id" %s' % i)

def set_variables(cfg):
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    shelltools.export("CC", "gcc %s" % cfg["coreflags"])
    shelltools.export("CXX", "g++ %s" % cfg["coreflags"])

    shelltools.export("CFLAGS", cfg["buildflags"])
    shelltools.export("CXXFLAGS", cfg["buildflags"])


### functionize repetetive tasks ###
def libcSetup(cfg):
    set_variables(cfg)

    if not os.path.exists(cfg["builddir"]):
        shelltools.makedirs(cfg["builddir"])

    shelltools.cd(cfg["builddir"])
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
                       --disable-profile \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --libexecdir=/usr/lib/misc \
                       %s " % cfg["extraconfig"])

def libcBuild(cfg):
    set_variables(cfg)

    shelltools.cd(cfg["builddir"])
    autotools.make()

def libcInstall(cfg):
    # not to bork locale/zone stuff
    set_variables(cfg)

    # install glibc/glibc-locale files
    shelltools.cd(cfg["builddir"])
    autotools.rawInstall("install_root=%s" % get.installDIR())

    # Some things want this, notably ash
    pisitools.dosym("libbsd-compat.a", "/usr/%s/libbsd.a" % cfg["libdir"])

    # Remove our options section from crt stuff
    removePardusSection("%s/usr/%s/" % (get.installDIR(), cfg["libdir"]))


### real actions start here ###
def setup():
    if multibuild:
        libcSetup(config["multiarch"])

    libcSetup(config["system"])


def build():
    if multibuild:
        libcBuild(config["multiarch"])

    libcBuild(config["system"])


# FIXME: yes fix me
#def check():
#    set_variables(cfg)
#    shelltools.chmod("scripts/begin-end-check.pl")
#
#    shelltools.cd("build")
#
#    shelltools.export("TIMEOUTFACTOR", "16")
#    autotools.make("-k check 2>error.log")


def install():
    # we do second arch first, to allow first arch to overwrite headers, etc.
    # stubs-32.h, elf.h, vm86.h comes only with 32bit
    if multibuild:
        libcInstall(config["multiarch"])
        pisitools.dosym("../lib32/ld-linux.so.2", "/lib/ld-linux.so.2")
        # FIXME: these should be added as additional file, when we can define pkg per arch
        pisitools.dodir("/etc/ld.so.conf.d")
        shelltools.echo("%s/etc/ld.so.conf.d/60-glibc-32bit.conf" % get.installDIR(), ldconf32bit)

    libcInstall(config["system"])

    # localedata can be shared between archs
    shelltools.cd(config["system"]["builddir"])
    autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

    # now we do generic stuff
    shelltools.cd(pkgworkdir)

    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        pisitools.remove("/etc/ld.so.cache")

    # It previously has 0755 perms which was killing things
    shelltools.chmod("%s/usr/%s/misc/pt_chown" % (get.installDIR(), config["system"]["libdir"]), 04711)

    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    # remove zoneinfo files since they are coming from timezone packages
    # we disable timezone build with a patch, keeping these lines for easier maintenance
    if shelltools.isDirectory("%s/usr/share/zoneinfo" % get.installDIR()):
        pisitools.removeDir("/usr/share/zoneinfo")

    for i in ["zdump", "zic"]:
        if shelltools.isFile("%s/usr/sbin/%s" % (get.installDIR(), i)):
            pisitools.remove("/usr/sbin/%s" % i)

    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "FAQ", "NEWS", "NOTES", "PROJECTS", "README*", "LICENSES")

