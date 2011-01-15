# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "vsFTP Server",
                 "tr": "vsFTP Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/vsftpd",
                 args="/etc/vsftpd/vsftpd.conf",
                 pidfile="/var/run/vsftpd.pid",
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/vsftpd",
                pidfile="/var/run/vsftpd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/vsftpd.pid")
