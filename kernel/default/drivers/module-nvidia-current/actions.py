# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

arch = get.ARCH().replace("i686", "x86")
version = get.srcVERSION()
driver = "nvidia-current"
base = "/usr/lib/%s" % driver

def setup():
    shelltools.system("sh NVIDIA-Linux-%s-%s.run -x --target tmp"
                      % (arch, get.srcVERSION()))
    shelltools.move("tmp/*", ".")

    # Our libc is TLS enabled so use TLS library
    shelltools.unlink("*-tls.so*")
    shelltools.move("tls/*", ".")

    # xorg-server provides libwfb.so
    shelltools.unlink("libnvidia-wfb.so.*")

    shelltools.echo("ld.so.conf", base)

def build():
    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("kernel")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.insinto("/lib/modules/%s/extra/nvidia" % KDIR,
                      "kernel/nvidia.ko", "%s.ko" % driver)

    # Command line tools and their man pages
    pisitools.dobin("nvidia-smi")
    pisitools.doman("nvidia-smi.1.gz")

    # Libraries
    pisitools.dolib("libGL.so.%s" % version, base)
    pisitools.dosym("libGL.so.%s" % version, "%s/libGL.so.1.2" % base)

    pisitools.dolib("libOpenCL.so.1.0.0", base)
    pisitools.dosym("libOpenCL.so.1.0.0", "%s/libOpenCL.so.1.0" % base)
    pisitools.dosym("libOpenCL.so.1.0", "%s/libOpenCL.so.1" % base)

    pisitools.dolib("libXvMCNVIDIA.so.%s" % version, base)
    pisitools.dosym("libXvMCNVIDIA.so.%s" % version, "%s/libXvMCNVIDIA.so.1" % base)
    pisitools.dosym("libXvMCNVIDIA.so.1", "%s/libXvMCNVIDIA.so" % base)

    pisitools.dolib("libcuda.so.%s" % version, base)
    pisitools.dosym("libcuda.so.%s" % version, "%s/libcuda.so.1" % base)
    pisitools.dosym("libcuda.so.1", "%s/libcuda.so" % base)

    pisitools.dolib("libnvidia-cfg.so.%s" % version, base)
    pisitools.dosym("libnvidia-cfg.so.%s" % version, "%s/libnvidia-cfg.so.1" % base)

    pisitools.dolib("libnvidia-compiler.so.%s" % version, base)
    pisitools.dosym("libnvidia-compiler.so.%s" % version, "%s/libnvidia-compiler.so.1" % base)

    for lib in ("glcore", "tls"):
        pisitools.dolib("libnvidia-%s.so.%s" % (lib, version), base)

    # VDPAU driver
    pisitools.dolib("libvdpau_nvidia.so.%s" % version, "%s/vdpau" % base)
    pisitools.dosym("../nvidia-current/vdpau/libvdpau_nvidia.so.%s" % version, "/usr/lib/vdpau/libvdpau_nvidia.so.1")

    # X modules
    pisitools.dolib("nvidia_drv.so", "%s/modules/drivers" % base)
    pisitools.dolib("libglx.so.%s" % version, "%s/modules/extensions" % base)
    pisitools.dosym("libglx.so.%s" % version, "%s/modules/extensions/libglx.so" % base)

    pisitools.insinto("/etc/OpenCL/vendors", "nvidia.icd")

    pisitools.insinto("/usr/share/nvidia-current", "ld.so.conf")

    # Documentation
    docdir = "xorg-video-%s" % driver
    pisitools.dodoc("LICENSE", "NVIDIA_Changelog", "README.txt", destDir=docdir)
    pisitools.dohtml("html/*", destDir=docdir)
