#!/usr/bin/python

import os
import glob

unopkg = "/opt/OpenOffice.org/bin/unopkg"
extPath = glob.glob("/opt/OpenOffice.org/lib/ooo-*/share/extension/install")[0]
extName = "wiki-publisher"
extID = "com.sun.wiki-publisher"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["JAVA_HOME"] = "/opt/sun-jre"
    ret = os.system("%s add --shared --force %s/%s.oxt" % (unopkg, extPath, extName))

    if ret != 0:
        raise Exception("Could not install OO.org extension: %s" % extName)

def preRemove():
    os.environ["JAVA_HOME"] = "/opt/sun-jre"
    ret = os.system("%s remove --shared %s" % (unopkg, extID))

    if ret != 0:
        raise Exception("Could not remove OO.org extension: %s" % extName)
