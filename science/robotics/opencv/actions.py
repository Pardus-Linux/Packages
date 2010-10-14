#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "OpenCV-%s" % get.srcVERSION()
shelltools.export("PYTHONDONTWRITEBYTECODE", "")

def setup():

    #temporary workaround for error: "'UINT64_C' was not declared in this scope"
    shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())

    cmaketools.configure("-DBUILD_EXAMPLES=1 \
                          -DBUILD_SWIG_PYTHON_SUPPORT=1 \
                          -DINSTALL_C_EXAMPLES=1 \
                          -DINSTALL_PYTHON_EXAMPLES=1 \
                          -DINSTALL_OCTAVE_EXAMPLES=1 \
                          -DWITH_FFMPEG=1 \
                          -DWITH_UNICAP=0 \
                          -DENABLE_OPENMP=0 \
                          -DNEW_PYTHIN_SUPPORT=1 \
                          -DOCTAVE_SUPPORT=0 \
                          -DUSE_MMX=1 \
                          -DUSE_SSE2=1 \
                          -DUSE_SSE3=0 \
                          -DUSE_SSE=1 \
                          -DWITH_1394=1 \
                          -DWITH_GSTREAMER=1 \
                          -DWITH_GTK=1 \
                          -DWITH_JASPER=1 \
                          -DWITH_JPEG=1 \
                          -DWITH_PNG=1 \
                          -DWITH_TIFF=1 \
                          -DWITH_V4L=1 \
                          -DWITH_XINE=1 \
                          -DCMAKE_SKIP_RPATH=1")
                          #  -DUSE_O3=OFF
                          #  -DUSE_OMIT_FRAME_POINTER=OFF


# upstream says tests fail due to library path, exporting here is kind of dangerous so disable for now
#def check():
#    cmaketools.make("test")

def build():
    cmaketools.make("VERBOSE=1")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR()) 

    # Move other docs and samples under standart doc dir
    doc_dir = "usr/share/doc/" + get.srcNAME()
    pisitools.domove("usr/share/opencv/doc", doc_dir)
    pisitools.domove("usr/share/opencv/samples", doc_dir)

    pisitools.dodoc("doc/license.txt")

