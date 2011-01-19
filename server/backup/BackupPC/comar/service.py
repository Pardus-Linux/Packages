#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "BackupPC server",
                 "tr": "BackupPC sunucusu"})

from comar.service import *

@synchronized
def start():
    startService("/usr/share/BackupPC/bin/BackupPC",
                 args="-d",
                 pidfile="/var/log/BackupPC/BackupPC.pid",
                 chuid="apache",
                 donotify=True)

@synchronized
def stop():
    stopService("/var/log/BackupPC/BackupPC.pid")

def status():
    return isServiceRunning("/var/log/BackupPC/BackupPC.pid")
