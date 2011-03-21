#!/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/mkdir -p /var/svn/repos/default")
    os.system("/usr/bin/svnadmin create /var/svn/repos/default")
    os.system("/bin/chown -Rf svn:svn /var/svn")
    os.system("/bin/chmod -Rf 774 /var/svn/repos")
    os.system("/bin/chmod 775 /var/svn/repos")
