#!/usr/bin/python

import os

libdir = "/usr/lib/xorg/modules/extensions"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install   %(libdir)s/libvnc.so  libvnc /usr/lib/xorg/libvnc.so  50 \
                --slave     /usr/bin/Xvnc   xvnc /usr/bin/xorg/Xvnc"
              % {"libdir": libdir})

def preRemove():
    os.system("/usr/sbin/alternatives   --remove   libvnc /usr/lib/xorg/libvnc.so")
