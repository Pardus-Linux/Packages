#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import subprocess

def dotexmfupdate(metapath):
    doc = piksemel.parse(metapath)
    for item in doc.tags("Source"):
        sourcename = item.getTagData("Name")
        if sourcename.startswith("texlive-"):
            subprocess.call(["/usr/bin/texmf-update"])
            return

def setupPackage(metapath, filepath):
    dotexmfupdate(metapath)

def cleanupPackage(metapath, filepath):
    dotexmfupdate(metapath)

