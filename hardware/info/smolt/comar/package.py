#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    UUID = file("/proc/sys/kernel/random/uuid").read().strip()
    file("/etc/hw-uuid", "w").write(UUID)
