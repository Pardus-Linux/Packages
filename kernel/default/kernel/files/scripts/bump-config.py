#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage:
# bump-config ARCH will bring overwrite pardus/configs/kernel-ARCH-config with the .config from /var/pisi

import os
import sys
import pisi
import shutil

if __name__ == "__main__":

    kpspec = pisi.specfile.SpecFile('pspec.xml')
    kpath = "/var/pisi/%s-%s-%s/work/%s" % (kpspec.source.name, kpspec.history[0].version,
                                            kpspec.history[0].release,
                                            kpspec.source.archive[0].name.split('.tar.bz2')[0])

    arch = "i686"
    try:
        arch = sys.argv[1]
    except IndexError:
        print "Architecture is %s" % arch

    if os.path.exists(kpath):
        shutil.copy(os.path.join(kpath, ".config"), "files/pardus/configs/kernel-%s-config" % arch)
    else:
        print "%s doesn't exist." % kpath
