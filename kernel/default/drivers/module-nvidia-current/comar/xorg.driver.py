# -*- coding: utf-8 -*-

import subprocess

from zorg.config import getDeviceInfo

driver = "nvidia-current"
base = "/usr/lib/%s" % driver


#
# Çomar methods
#

def enable():
    subprocess.call(["/usr/sbin/alternatives", "--set", "libGL", "%s/libGL.so.1.2" % base])
    subprocess.call(["/sbin/ldconfig", "-X"])

def disable():
    subprocess.call(["/usr/sbin/alternatives", "--set", "libGL", "/usr/lib/mesa/libGL.so.1.2"])
    subprocess.call(["/sbin/ldconfig", "-X"])

def getInfo():
    info = {
            "alias":        driver,
            "xorg-module":  "nvidia"
            }
    return info

def getDeviceOptions(busId, options):
    dev = getDeviceInfo(busId)
    if not dev:
        return options

    ignoredDisplays = []
    enabledDisplays = []
    horizSync = []
    vertRefresh = []
    metaModes = []
    rotation = ""
    orientation = ""
    order = ""

    for name, output in dev.outputs.items():
        if output.ignored:
            ignoredDisplays.append(name)
            continue

        if output.enabled:
            enabledDisplays.append(name)
        else:
            continue

        if name in dev.monitors:
            mon = dev.monitors[name]
            horizSync.append("%s: %s" % (name, mon.hsync))
            vertRefresh.append("%s: %s" % (name, mon.vref))

        if output.mode:
            if output.refresh_rate:
                metaModes.append("%s: %s_%s" % (name, output.mode, output.refresh_rate))

            metaModes.append("%s: %s" % (name, output.mode))
        else:
            metaModes.append("%s: nvidia-auto-select" % name)

        if output.rotation and not rotation:
            rotation = output.rotation

        if output.right_of:
            orientation = "%s RightOf %s" % (name, output.right_of)
            order = "%s, %s" % (output.right_of, name)
        elif output.below:
            orientation = "%s Below %s" % (name, output.below)
            order = "%s, %s" % (output.below, name)

    if ignoredDisplays:
        options["IgnoreDisplayDevices"] = ", ".join(ignoredDisplays)

    if horizSync:
        options["HorizSync"] = "; ".join(horizSync)
        options["VertRefresh"] = "; ".join(vertRefresh)

    if metaModes:
        options["MetaModes"] = ", ".join(metaModes)

    if rotation:
        options["Rotate"] = rotation

    if orientation:
        options["TwinView"] = "True"
        options["TwinViewOrientation"] = orientation
        options["TwinViewXineramaInfoOrder"] = order
    elif len(enabledDisplays) > 1:
        options["TwinView"] = "True"
        options["TwinViewOrientation"] = "%s Clone %s" % tuple(enabledDisplays[:2])

    return options
