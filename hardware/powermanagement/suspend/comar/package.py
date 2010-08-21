#/usr/bin/python

import os

suspendConf = """# Auto generated suspend.conf
# your snapshot device. You should not need to change this.
snapshot device = /dev/snapshot

# enter your swap device here.
resume device = %s

# compression will often speed up suspend and resume
compress = y

#image size = 350000000

# Debugging option
#suspend loglevel = 2

# compute checksum will slow down suspend and resume. Debugging option
#compute checksum = y

## encryption support is rather basic right now - e.g. USB keyboards will not
## work to enter the key in the standard initrd, also beware of
## non-US keyboard layouts. Only use this if you know what you are doing.
#encrypt = y
#early writeout = n
#splash = y
"""

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/etc/suspend.conf"):
        # this approach relies on YALI's resume= feature
        f = file("/proc/cmdline", "r")
        try:
           resumeDevice = f.readline().split("resume=")[1].split()[0]
        except IndexError:
            resumeDevice = None
        f.close()

        if resumeDevice != None:
            f = file("/etc/suspend.conf", "w")
            f.write(suspendConf % resumeDevice)
            f.close()
