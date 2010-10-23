# -*- coding: utf-8 -*-

import subprocess


#
# Çomar methods
#

def enable():
    subprocess.call(["/usr/sbin/alternatives", "--set", "libGL", "/usr/lib/fglrx/libGL.so.1.2"])

def disable():
    subprocess.call(["/usr/sbin/alternatives", "--set", "libGL", "/usr/lib/mesa/libGL.so.1.2"])

def getInfo():
    info = {
            "alias":        "fglrx",
            "xorg-module":  "fglrx"
            }
    return info

def getDeviceOptions(busId, options):
    return options
