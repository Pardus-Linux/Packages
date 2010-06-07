# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "System Message Logger",
                 "tr": "Sistem Mesaj Günlükleyicisi"})
serviceDefault = "on"

@synchronized
def start():
    startService(command="/usr/sbin/syslogd",
                 args=config.get("SYSLOGD", "-m 15"),
                 pidfile="/var/run/syslogd.pid",
                 detach=True)

    waitBus("/dev/log", stream=False)

    startService(command="/usr/sbin/klogd",
                 args=config.get("KLOGD", "-c 3 -2"),
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/klogd.pid")
    stopService(pidfile="/var/run/syslogd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/syslogd.pid") and isServiceRunning("/var/run/klogd.pid")
