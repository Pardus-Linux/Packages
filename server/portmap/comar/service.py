# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Portmap Daemon",
                 "tr": "Portmap Servisi"})

@synchronized
def start():
    startService(command="/sbin/portmap",
                 args=config.get("PORTMAP_OPTS",""),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/sbin/portmap",
                donotify=True)

def status():
    return isServiceRunning(command="/sbin/portmap")
