#!/usr/bin/python

import os

base = "/usr/lib/nvidia173"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install /usr/lib/libGL.so.1.2 libGL %(base)s/libGL.so.1.2 40 \
                --slave /usr/lib/xorg/modules/volatile xorg-modules-volatile %(base)s/modules \
                --slave /etc/ld.so.conf.d/10-nvidia173.conf nvidia173-conf /usr/share/nvidia173/ld.so.conf"
              % {"base" : base})

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2" % base)
    pass
