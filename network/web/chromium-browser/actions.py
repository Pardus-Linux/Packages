#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "chromium-%s" % get.srcVERSION()

shelltools.export("HOME", get.workDIR())

ARCH = "x64" if get.ARCH() == "x86_64" else "ia32"

def setup():
    #TODO use_system_ssl is disabled -->  https://bugzilla.mozilla.org/show_bug.cgi?id=547312
    #TODO use_system_sqlite is faulty --> http://crbug.com/22208

    shelltools.system("build/gyp_chromium -f make build/all.gyp --depth=. \
                        -Dgcc_version=44 \
                        -Dno_strict_aliasing=1 \
                        -Dwerror= \
                        -Dlinux_strip_binary=1 \
                        -Dlinux_sandbox_path=/usr/lib/chrome/chromium_sandbox \
                        -Dlinux_sandbox_chrome_path=/usr/lib/chromium-browser/chromium-browser \
                        -Drelease_extra_cflags=-fno-ipa-cp \
                        -Dproprietary_codecs=1 \
                        -Duse_system_bzip2=1 \
                        -Duse_system_libpng=1 \
                        -Duse_system_libevent=1 \
                        -Duse_system_libjpeg=1 \
                        -Duse_system_libxslt=1 \
                        -Duse_system_zlib=1 \
                        -Duse_system_ffmpeg=1 \
                        -Duse_system_libxml=1 \
                        -Duse_system_sqlite=0 \
                        -Duse_system_yasm=1 \
                        -Duse_system_ssl=0 \
                        -Duse_system_icu=1 \
                        -Duse_system_hunspell=1 \
                        -Ddisable_sse2=1 \
                        -Dtarget_arch=%s" % ARCH)

def build():
    autotools.make("chrome chrome_sandbox BUILDTYPE=Release")

def install():
    shelltools.cd("out/Release")

    shelltools.makedirs("%s/usr/lib/chromium-browser" % get.installDIR())

    pisitools.insinto("/usr/lib/chromium-browser", "chrome.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "resources.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome", "chromium-browser")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome_sandbox")
    pisitools.insinto("/usr/lib/chromium-browser", "xdg-settings")
    pisitools.insinto("/usr/lib/chromium-browser", "locales")
    pisitools.insinto("/usr/lib/chromium-browser", "resources")

    pisitools.newman("chrome.1", "chromium-browser.1")

    shelltools.cd("../..")
    for size in ["16", "22", "24", "32", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")

