#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def updateGIOModuleCache(filepath):
    parse = piksemel.parse(filepath)
    GIO_MODULE_PATH = "usr/lib/gio/modules"
    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith(GIO_MODULE_PATH):
            os.system("/usr/bin/gio-querymodules /%s" % GIO_MODULE_PATH)
            return

def setupPackage(metapath, filepath):
    updateGIOModuleCache(filepath)

def postCleanupPackage(metapath, filepath):
    updateGIOModuleCache(filepath)
