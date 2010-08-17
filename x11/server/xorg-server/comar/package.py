#!/usr/bin/python

import os

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

def ensureLink(target, link):
    if not os.path.exists(link):
        symlink(target, link)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    ensureLink("../../std/extensions/libglx.so",    "/usr/lib/xorg/modules/extensions/libglx.so")
