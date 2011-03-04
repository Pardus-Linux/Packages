# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDefault = "off" #NM starts wpa_supp automatically. Use at your own risk if you start manually
serviceDesc = _({"en": "WPA Daemon",
                 "tr": "WPA Hizmeti"})

pidfile = "/var/run/wpa_supplicant.pid"

@synchronized
def start():
    startService(command="/usr/sbin/wpa_supplicant",
                 args="-WuB -P%s %s" % (pidfile, config.get("OPTS", "")),
                 pidfile=pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
