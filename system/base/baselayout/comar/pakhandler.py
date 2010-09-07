# -*- coding: utf-8 -*-

import piksemel
import subprocess

def update_ld_so_cache(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("etc/ld.so.conf.d"):
            subprocess.call(["/sbin/ldconfig", "-X"])
            return

def setupPackage(metapath, filepath):
    update_ld_so_cache(filepath)

def postCleanupPackage(metapath, filepath):
    update_ld_so_cache(filepath)
