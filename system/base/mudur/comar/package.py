#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # add disks into fstsb
    os.system("/sbin/update-fstab")
