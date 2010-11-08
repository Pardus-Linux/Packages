#!/usr/bin/python

import os

unopkg = "/usr/bin/unopkg"
extID = "net.zemberek.ooo.spellchecker"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    import glob

    extPath = glob.glob("/usr/share/zemberek/zemberek*.oxt")[0]
    os.environ["JAVA_HOME"] = "/opt/sun-jre"

    ret = os.system("%s add --shared --force %s" % (unopkg, extPath))

    if ret != 0:
        print "Could not install OO.org extension: %s" % extID

def preRemove():
    os.environ["JAVA_HOME"] = "/opt/sun-jre"

    ret = os.system("%s remove --shared %s" % (unopkg, extID))

    if ret != 0:
        print "Removing OO extension %s failed." % extID
