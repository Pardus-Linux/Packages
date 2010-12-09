#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip=["/usr/share/qemu"]

# Disabled linux-user targets: m68k, ppc, ppc64, ppc64abi32, sh4, sh4eb
# user_targets=["alpha","arm","armeb","cris","i386","mips","mipsel","sparc","sparc32plus","sparc64", "x86_64"]

# Disabled softmmu targets (in addition to above) : alpha, arm, armeb
# soft_targets=["cris","i386","mips","mipsel","sparc","sparc32plus","sparc64", "x86_64"]

# target_list=[]

# for target in user_targets:
#     target_list.append("%s-linux-user" % target)

# for target in soft_targets:
#     target_list.append("%s-softmmu" % target)


cflags = get.CFLAGS().replace("-fpie", "").replace("-fstack-protector", "")
#extraldflags="-Wl,--build-id"
#buildldflags="VL_LDFLAGS=-Wl,--build-id"
extraldflags=""
buildldflags=""

soundDrivers = "pa sdl alsa oss"

targetlist = "i386-softmmu x86_64-softmmu arm-softmmu cris-softmmu m68k-softmmu \
              mips-softmmu mipsel-softmmu mips64-softmmu mips64el-softmmu ppc-softmmu \
              ppcemb-softmmu ppc64-softmmu sh4-softmmu sh4eb-softmmu sparc-softmmu \
              i386-linux-user x86_64-linux-user alpha-linux-user arm-linux-user \
              armeb-linux-user cris-linux-user m68k-linux-user mips-linux-user \
              mipsel-linux-user ppc-linux-user ppc64-linux-user ppc64abi32-linux-user \
              sh4-linux-user sh4eb-linux-user sparc-linux-user sparc64-linux-user \
              sparc32plus-linux-user"


def setup():
    # disable fdt until dtc is in repo
    # pisitools.dosed("configure", 'fdt="yes"', 'fdt="no"')

    shelltools.export("CFLAGS", cflags)
    shelltools.export("LC_ALL", "en_US.UTF-8")
    autotools.rawConfigure('--prefix=/usr \
                            --mandir=/usr/share/man \
                            --sysconfdir=/etc \
                            --disable-werror \
                            --disable-strip \
                            --disable-kvm \
                            --disable-bsd-user \
                            --disable-darwin-user \
                            --target-list="%s" \
                            --audio-drv-list="%s" \
                            --cc="%s" \
                            --host-cc="%s" \
                            --extra-ldflags="%s" \
                            --extra-cflags="%s" '% (targetlist, soundDrivers, get.CC(), get.CC(), extraldflags, cflags))


                            #--enable-system \
                            #--enable-linux-user \

                            # --audio-card-list="ac97 es1370 sb16 cs4231a adlib gus" \
                            # --target-list="%s"' % " ".join(target_list))
                            # --disable-bluez \
                            # --kerneldir="/lib/modules/%s/build" \

def build():
    shelltools.export("LC_ALL", "en_US.UTF-8")
    autotools.make("V=1 -j1 %s" % buildldflags)

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # comes with kvm
    pisitools.remove("/usr/bin/qemu-io")

    for i in ["pc-bios/README", "LICENSE", "TODO", "README", "qemu-doc.html", "qemu-tech.html"]:
        pisitools.dodoc(i)

