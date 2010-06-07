#!/usr/bin/python
import os
import glob
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if fromVersion == "3.3_pre11":
        # Upgrading from Pardus 2008
        for f in [_f for _f in glob.glob("/etc/modprobe.d/*") if not _f.endswith(".conf")]:
            # Remove old files
            os.unlink(f)

def preRemove():
    pass
