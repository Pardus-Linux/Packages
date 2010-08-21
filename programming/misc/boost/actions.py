# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "boost-cmake-%s" % get.srcVERSION()

def setup():
    cmaketools.configure("-DBUILD_EXAMPLES=NONE \
                          -DBUILD_PROJECTS=ALL \
                          -DBUILD_SOVERSIONED=ON \
                          -DBUILD_TESTS=NONE \
                          -DBUILD_TOOLS=NONE \
                          -DENABLE_DEBUG=OFF \
                          -DENABLE_MULTI_THREADED=ON \
                          -DENABLE_RELEASE=ON \
                          -DENABLE_SHARED=ON \
                          -DENABLE_SINGLE_THREADED=ON \
                          -DENABLE_STATIC=OFF \
                          -DINSTALL_VERSIONED=OFF \
                          -DWITH_BZIP2=ON \
                          -DWITH_DOXYGEN=ON \
                          -DWITH_EXPAT=ON \
                          -DWITH_ICU=ON \
                          -DWITH_MPI=ON \
                          -DWITH_PYTHON=ON \
                          -DWITH_VALGRIND=OFF \
                          -DWITH_XSLTPROC=ON \
                          -DWITH_ZLIB=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    # Remove .cmake files used to build boost
    pisitools.remove("/usr/lib/*.cmake")

    # Remove cmake modules. We will use cmake's FindBoost.
    pisitools.removeDir("/usr/share/boost-*")
    pisitools.removeDir("/usr/share/cmake")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("LICENSE*")
