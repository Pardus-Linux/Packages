#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

KeepSpecial=["perl"]

def setup():
    shelltools.export("LC_ALL", "C")

    shelltools.system('sh Configure -des \
                      -Darchname=%s-linux \
                      -Dcccdlflags=-fPIC \
                      -Dccdlflags=-rdynamic \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize="%s" \
                      -Duselargefiles \
                      -Dd_dosuid \
                      -Dusethreads \
                      -Duseithreads \
                      -Dd_semctl_semun \
                      -Dscriptdir=/usr/bin \
                      -Dman1dir=/usr/share/man/man1 \
                      -Dman3dir=/usr/share/man/man3 \
                      -Dinstallman1dir=%s/usr/share/man/man1 \
                      -Dinstallman3dir=%s/usr/share/man/man3 \
                      -Dlibperl=libperl.so.1.5.8 \
                      -Duseshrplib \
                      -Dman1ext=1 \
                      -Dman3ext=3pm \
                      -Dcf_by=Pardus \
                      -Ud_csh \
                      -Di_ndbm \
                      -Di_gdbm \
                      -Di_db \
                      -Ubincompat5005 \
                      -Uversiononly \
                      -Dpager="/usr/bin/less -isr" \
                      -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
                      -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
                      -Ud_endservent_r_proto -Ud_setservent_r_proto \
                      ' %(get.ARCH(), get.CC(), get.CFLAGS(), get.installDIR(), get.installDIR()))

def build():
    # colorgcc uses Term::ANSIColor
    paths = get.ENV("PATH").split(":")
    if "/usr/share/colorgcc" in paths:
        paths.remove("/usr/share/colorgcc")
    shelltools.export("PATH", ":".join(paths))
    ##
    autotools.make()

def check():
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/perl")
    pisitools.remove("/usr/bin/suidperl")
    # Conflicts with perl-Module-Build
    pisitools.remove("/usr/bin/config_data")

    pisitools.dosym("/usr/bin/perl5.10.1", "/usr/bin/perl")
    pisitools.dosym("/usr/bin/sperl5.10.1", "/usr/bin/suidperl")

    # Perl5 library
    pisitools.dosym("/usr/lib/perl5/5.10.1/%s-linux-thread-multi/CORE/libperl.so.1.5.8" % get.ARCH(), "/usr/lib/libperl.so")
    pisitools.dosym("/usr/lib/perl5/5.10.1/%s-linux-thread-multi/CORE/libperl.so.1.5.8" % get.ARCH(), "/usr/lib/libperl.so.1")
    pisitools.dosym("/usr/lib/perl5/5.10.1/%s-linux-thread-multi/CORE/libperl.so.1.5.8" % get.ARCH(), "/usr/lib/libperl.so.1.5")
    pisitools.dosym("/usr/lib/perl5/5.10.1/%s-linux-thread-multi/CORE/libperl.so.1.5.8" % get.ARCH(), "/usr/lib/libperl.so.1.5.8")

    # Remove duplicated docs
    pisitools.remove("/usr/share/man/man3/Digest::MD5.3pm")
    pisitools.remove("/usr/share/man/man3/Digest.3pm")
    pisitools.remove("/usr/share/man/man3/Digest::base.3pm")
    pisitools.remove("/usr/share/man/man3/Digest::file.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Netrc.3pm")
    pisitools.remove("/usr/share/man/man3/Net::libnetFAQ.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Config.3pm")
    pisitools.remove("/usr/share/man/man3/Net::FTP.3pm")
    pisitools.remove("/usr/share/man/man3/Net::NNTP.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Time.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Domain.3pm")
    pisitools.remove("/usr/share/man/man3/Net::POP3.3pm")
    pisitools.remove("/usr/share/man/man3/Net::SMTP.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Cmd.3pm")
    pisitools.remove("/usr/share/man/man3/MIME::Base64.3pm")
    pisitools.remove("/usr/share/man/man3/MIME::QuotedPrint.3pm")
    pisitools.remove("/usr/share/man/man3/Time::HiRes.3pm")
    pisitools.remove("/usr/share/man/man3/Getopt::Long.3pm")
    pisitools.remove("/usr/share/man/man3/IO::Zlib.3pm")

    # perl-Archive-Tar
    pisitools.remove("/usr/share/man/man3/Archive::Tar.3pm")
    pisitools.remove("/usr/share/man/man3/Archive::Tar::File.3pm")
    pisitools.remove("/usr/share/man/man1/ptar.1")
    pisitools.remove("/usr/share/man/man1/ptardiff.1")

    # Docs
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    shelltools.system('LD_LIBRARY_PATH=%s ./perl installhtml \
                       --podroot="." \
                       --podpath="lib:ext:pod:vms" \
                       --recurse \
                       --htmldir="%s/usr/share/doc/%s/html" \
                       --libpods="perlfunc:perlguts:perlvar:perlrun:perlop"' % (get.curDIR(), get.installDIR(), get.srcNAME()))

    pisitools.dodoc("Changes*", "Artistic", "Copying", "README", "AUTHORS")
