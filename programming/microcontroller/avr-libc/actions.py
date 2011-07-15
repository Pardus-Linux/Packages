#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"
TOOLCHAIN_DIR="/opt/toolchain/avr"

def check_supported_mcus():
    # bash scriptingin gozunu seviyim
    import os
    mcu_list = os.popen(r"sed -n -r '/CHECK_AVR_DEVICE/{s:.*[(](.*)[)]:\1:;p}' configure.ac").read().split()[1:]
    for mcu in mcu_list:
        print " ==> checking for %s... " % mcu
        ret = os.system('avr-gcc -E - -mmcu=%s <<<"" |& grep -q \'unknown MCU\'' % mcu)
        if ret <= 0:
            print "     E: %s is not supported!" % mcu
            pisitools.dosed('configure', 'HAS_%s=yes' % mcu, 'HAS_%s=no' % mcu)

    return 0

def setup():
    # Force cross compile to avr target
    shelltools.export("CC", "avr-gcc")
    shelltools.export("PATH", "%s:%s/bin" % (get.ENV("PATH"), TOOLCHAIN_DIR))

    check_supported_mcus()

    # FIXME --enable-doc
    shelltools.system(" \
            ./configure \
            --prefix=/opt/toolchain/avr \
            --build=%s \
            --host=avr" % get.HOST())

def build():
    shelltools.export("LC_ALL", "C")
    shelltools.export("PATH", "%s:%s/bin" % (get.ENV("PATH"), TOOLCHAIN_DIR))

    autotools.make()

def install():
    shelltools.export("PATH", "%s:/opt/toolchain/avr/bin" % get.ENV("PATH"))
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
