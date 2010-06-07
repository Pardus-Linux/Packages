#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.popen("/sbin/init U &> /dev/null")
