#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.export("LDFLAGS","%s -shared" % get.LDFLAGS())

    # Fix for import scipy.linalg: ImportError: /usr/lib/python2.6/site-packages/scipy/linalg/clapack.so: undefined symbol: clapack_sgesv
    shelltools.export("ATLAS", "None")
    shelltools.export("UMFPACK", "/usr/lib")
    shelltools.export("FFTW", "/usr/lib")
    shelltools.export("BLAS", "/usr/lib")
    shelltools.export("LAPACK", "/usr/lib")

    pythonmodules.install()

    pisitools.dodoc("LICENSE.txt","THANKS.txt","TOCHANGE.txt")
