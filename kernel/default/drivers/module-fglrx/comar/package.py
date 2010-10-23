#!/usr/bin/python

import os

base = "/usr/lib/fglrx"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install /usr/lib/libGL.so.1.2 libGL %(base)s/libGL.so.1.2 50 \
                --slave /usr/lib/xorg/modules/volatile xorg-modules-volatile %(base)s/modules"
              % {"base" : base})

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2" % base)
    pass
