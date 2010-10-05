# -*- coding: utf-8 -*-

import piksemel
import subprocess

def domodules(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("usr/share/man/"):
            subprocess.call(["/usr/bin/mandb", ])
            return

def setupPackage(metapath, filepath):
    domodules(filepath)

def postCleanupPackage(metapath, filepath):
    domodules(filepath)
