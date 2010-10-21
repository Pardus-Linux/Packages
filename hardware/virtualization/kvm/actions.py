#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip=["/usr/share/kvm"]
WorkDir="qemu-kvm-%s" % get.srcVERSION()

cflags = get.CFLAGS().replace("-fpie", "").replace("-fstack-protector", "")

targetList = "i386-softmmu i386-linux-user"

def setup():
    # disable fdt until dtc is in repo
    # pisitools.dosed("configure", 'fdt="yes"', 'fdt="no"')

    shelltools.export("CFLAGS", cflags)
    autotools.rawConfigure('--prefix=/usr \
                            --audio-drv-list="alsa pa sdl oss" \
                            --cc="%s" \
                            --host-cc="%s" \
                            --enable-system \
                            --enable-linux-user \
                            --disable-strip \
                            --disable-bsd-user \
                            --disable-darwin-user' % (get.CC(), get.CC()))

    shelltools.cd("kvm/user")
    autotools.rawConfigure("--prefix=/usr \
                            --kerneldir=../../kernel")


def build():
    autotools.make("V=1")
    autotools.make("-C kvm/user kvmtrace")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/qemu-system-x86_64", "/usr/bin/", "qemu-kvm")
    pisitools.domove("/usr/share/man/man1/qemu.1", "/usr/share/man/man1/", "qemu-kvm.1")

    # Install kvm-tools
    pisitools.dobin("kvm/user/kvmtrace")
    pisitools.dobin("kvm/user/kvmtrace_format")
    pisitools.dobin("kvm/kvm_stat")

    # Use the one qemu provides
    pisitools.remove("/usr/bin/qemu-img")
    pisitools.remove("/usr/share/man/man1/qemu-img.1")
    pisitools.remove("/usr/bin/qemu-nbd")

    pisitools.removeDir("/usr/share/man/man8/")
    pisitools.removeDir("/usr/share/doc")
