#!/usr/bin/python

import os
import subprocess

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    libGL = "/usr/lib/libGL.so.1.2"
    if not os.path.exists(libGL) or os.readlink(libGL).startswith("xorg/std"):
        # GL library
        symlink("mesa/libGL.so.1.2", libGL)

        # Create other links
        subprocess.call(["/sbin/ldconfig"])

        # We do not use .la files anymore
        unlink("/usr/lib/libGL.la")
