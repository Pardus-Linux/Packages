#!/usr/bin/python

import os

xmlCat = "/etc/xml/catalog"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    if not os.path.exists(xmlCat):
        if not os.path.exists("/etc/xml"):
            os.mkdir("/etc/xml")

        f = open(xmlCat, "w")

        p = os.popen("/usr/bin/xmlcatalog --create", "r")
        f.writelines(p.readlines())

        f.close()
        p.close()
