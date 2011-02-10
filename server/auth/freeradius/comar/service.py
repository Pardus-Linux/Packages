#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "FreeRadius Server",
                 "tr": "FreeRadius Sunucusu"})

serviceConf = "freeradius"
PIDFILE = "/var/run/radiusd/radiusd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/radiusd",
                 args="-X -f",
                 pidfile=PIDFILE,
                 donotify=True,
                 detach=True,
                 makepid=True,
                 chuid="radiusd:radiusd")

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
