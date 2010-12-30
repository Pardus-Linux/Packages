# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure("--enable-pic \
                         --disable-xcb \
                         --enable-glx-tls \
                         --disable-gl-osmesa \
                         --disable-egl \
                         --disable-glw \
                         --disable-glut \
                         --enable-gallium \
                         --enable-gallium-llvm \
                         --disable-gallium-svga \
                         --disable-gallium-i915 \
                         --disable-gallium-i965 \
                         --enable-gallium-radeon \
                         --disable-gallium-r600 \
                         --disable-gallium-nouveau \
                         --with-driver=dri \
                         --with-dri-driverdir=/usr/lib/xorg/modules/dri \
                         --with-dri-drivers=i810,i915,i965,mach64,r128,r200,r600,radeon,sis,tdfx \
                         --with-state-trackers=dri,glx")

    pisitools.dosed("configs/autoconf", "(PYTHON_FLAGS) = .*", r"\1 = -t")

def build():
    autotools.make("-C src/glsl glsl_lexer.cpp")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use llvmpipe instead of classic swrast driver
    pisitools.rename("/usr/lib/xorg/modules/dri/swrastg_dri.so", "swrast_dri.so")

    # Don't install unused headers
    #for header in ("[a-fh-wyz]*.h", "glf*.h"):
    for header in ("[a-fh-wyz]*.h", "glf*.h", "*glut*.h"):
        pisitools.remove("/usr/include/GL/%s" % header)

    # Moving libGL for dynamic switching
    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/mesa")

    pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
