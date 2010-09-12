# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

libdir = "/usr/lib/llvm"

def setup():
    pisitools.dosed("tools/llvm-config/llvm-config.in.in",
                    r'"(\$ABS_RUN_DIR/lib.*)"', r'"\1/llvm"')

    pic_option = "enable" if get.ARCH() == "x86_64" else "disable"

    autotools.configure("--libdir=%s \
                         --datadir=/usr/share/llvm \
                         --enable-optimized \
                         --disable-assertions \
                         --disable-expensive-checks \
                         --enable-debug-runtime \
                         --enable-debug-symbols \
                         --enable-jit \
                         --disable-doxygen \
                         --enable-threads \
                         --%s-pic \
                         --enable-shared \
                         --enable-targets=host \
                         --enable-bindings=all \
                         --enable-libffi \
                         --enable-llvmc-dynamic \
                         --enable-llvmc-dynamic-plugins \
                         " % (libdir, pic_option))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          PROJ_etcdir=/etc/llvm \
                          PROJ_libdir=%s \
                          PROJ_docsdir=/%s/llvm"
                          % (get.installDIR(), libdir, get.docDIR()))

    # Remove executable bit from static libs
    shelltools.chmod("%s/usr/lib/*/*.a" % get.installDIR(), 0644)

    # Remove example file
    pisitools.remove("/usr/lib/llvm/*LLVMHello.*")

    pisitools.remove("/usr/share/doc/llvm/*.tar.gz")
    pisitools.remove("/usr/share/doc/llvm/ocamldoc/html/*.tar.gz")
    pisitools.removeDir("/usr/share/doc/llvm/ps")

    pisitools.dodoc("CREDITS.TXT", "LICENSE.TXT", "README.txt")
