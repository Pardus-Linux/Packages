#!/usr/bin/python

import os
import glob

unopkg = "/usr/bin/unopkg"
extPath = glob.glob("/usr/share/zemberek/zemberek*.oxt")[0]
extID = "net.zemberek.ooo.spellchecker"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["JAVA_HOME"] = "/opt/sun-jre"

    ret = os.system("%s add --shared --force %s" % (unopkg, extPath))

    if ret != 0:
        raise Exception("Could not install OO.org extension: %s" % extID)

def preRemove():
    os.environ["JAVA_HOME"] = "/opt/sun-jre"

    ret = os.system("%s remove --shared %s" % (unopkg, extID))

    #if ret != 0:
    #    raise Exception("Could not remove OO.org extension: %s" % extID)
