#!/usr/bin/python

import os
import shutil

import pisi

def moveModules(fromVersion, toVersion):
    oldPath = "/usr/lib/perl5/vendor_perl/%s" % fromVersion
    newPath = "/usr/lib/perl5/vendor_perl/%s" % toVersion

    if os.path.islink(oldPath):
        return

    for module in os.listdir(oldPath):
        shutil.move("%s/%s" % (oldPath, module), "%s/%s" % (newPath, module))
    os.rmdir(oldPath)
    os.symlink(newPath, oldPath)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if fromVersion and pisi.version.Version(fromVersion) < pisi.version.Version(toVersion):
        moveModules(fromVersion, toVersion)
