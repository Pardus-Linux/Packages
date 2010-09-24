#!/usr/bin/python

import os
import stat
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Create device nodes in chroot
    CHROOT  = "/var/named/chroot"
    NODES   = {
                "/dev/random"    : [stat.S_IFCHR | 0666, 1, 8],
                "/dev/zero"      : [stat.S_IFCHR | 0666, 1, 5],
                "/dev/null"      : [stat.S_IFCHR | 0666, 1, 3],
              }
    for node, values in NODES.items():
        if not os.path.exists("%s%s" % (CHROOT, node)):
            os.mknod("%s%s" % (CHROOT, node), values[0], os.makedev(values[1], values[2]))

    try:
        os.unlink("%s/etc/localtime" % CHROOT)
    except:
        pass
    else:
        shutil.copy("/etc/localtime", "%s/etc/localtime" % CHROOT)
