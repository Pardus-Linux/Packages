#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/home/samba"):
        os.system("/bin/mkdir /home/samba")
        os.system("/bin/chmod 0777 /home/samba")

    os.system("/bin/chmod 0750 /var/lib/samba/winbindd_privileged")
