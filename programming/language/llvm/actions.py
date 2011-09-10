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
    shelltools.move("tools/clang-%s" % get.srcVERSION(), "tools/clang")

    pisitools.dosed("tools/llvm-config/llvm-config.in.in",
                    r'"(\$ABS_RUN_DIR/lib.*)"', r'"\1/llvm"')

    pic_option = "enable" if get.ARCH() == "x86_64" else "disable"

    options = "--libdir=%s \
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
               --with-binutils-include=/usr/include \
               --enable-libffi \
               --enable-llvmc-dynamic \
               --enable-llvmc-dynamic-plugins \
               " % (libdir, pic_option)

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"

        #shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())

    autotools.configure(options)


def check():
    autotools.make("check")
    autotools.make("-C tools/clang test")

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":

        autotools.rawInstall("DESTDIR=%s \
                              PROJ_etcdir=/etc/llvm \
                              PROJ_libdir=/usr/lib32/llvm \
                              PROJ_docsdir=/%s/llvm"
                              % (get.installDIR(),  get.docDIR()))
        pisitools.removeDir("/emul32")
        # Remove executable bit from static libs
        shelltools.chmod("%s/usr/lib32/*/*.a" % get.installDIR(), 0644)
        return
    else:
        autotools.rawInstall("DESTDIR=%s \
                              PROJ_etcdir=/etc/llvm \
                              PROJ_libdir=%s \
                              PROJ_docsdir=/%s/llvm"
                              % (get.installDIR(), libdir, get.docDIR()))


    # Install static analyzers which aren't installed by default
    for exe in ("scan-build", "scan-view"):
        pisitools.insinto("/usr/lib/clang-analyzer/%s" % exe, "tools/clang/tools/%s/%s" % (exe, exe))
        pisitools.dosym("/usr/lib/clang-analyzer/%s/%s" % (exe, exe), "/usr/bin/%s" % exe)

    pisitools.dodir("/etc/ld.so.conf.d")
    shelltools.echo("%s/etc/ld.so.conf.d/51-llvm.conf" % get.installDIR(), "/usr/lib/llvm")

    # Remove executable bit from static libs
    shelltools.chmod("%s/usr/lib/*/*.a" % get.installDIR(), 0644)

    # Remove example file
    pisitools.remove("/usr/lib/llvm/*LLVMHello.*")

    pisitools.remove("/usr/share/doc/llvm/*.tar.gz")
    pisitools.remove("/usr/share/doc/llvm/ocamldoc/html/*.tar.gz")
    pisitools.removeDir("/usr/share/doc/llvm/ps")

    pisitools.dodoc("CREDITS.TXT", "LICENSE.TXT", "README.txt")
