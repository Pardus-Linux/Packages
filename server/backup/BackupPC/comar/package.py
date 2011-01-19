#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R apache.apache /etc/BackupPC")
    os.system("/bin/chmod u-s /usr/share/BackupPC/cgi-bin/BackupPC_Admin")
