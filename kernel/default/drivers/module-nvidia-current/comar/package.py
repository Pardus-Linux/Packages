#!/usr/bin/python

import os

base = "/usr/lib/nvidia-current"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install /usr/lib/libGL.so.1.2 libGL %(base)s/libGL.so.1.2 50 \
                --slave /usr/lib/xorg/modules/volatile xorg-modules-volatile %(base)s/modules \
                --slave /etc/X11/XvMCConfig XvMCConfig /usr/share/nvidia-current/XvMCConfig \
                --slave /etc/ld.so.conf.d/10-nvidia-current.conf nvidia-current-conf /usr/share/nvidia-current/ld.so.conf"
              % {"base" : base})

    # If this driver is in use, refresh links after installation.
    if os.readlink("/etc/alternatives/libGL") == "%s/libGL.so.1.2" % base:
        os.system("/usr/sbin/alternatives --set libGL %s/libGL.so.1.2" % base)
        os.system("/sbin/ldconfig -X")

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2" % base)
    pass
