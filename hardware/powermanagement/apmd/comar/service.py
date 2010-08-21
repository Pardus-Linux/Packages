# -*- coding: utf-8 -*-
serviceType = "local"
serviceDesc = _({"en": "APM Daemon",
                 "tr": "APM Servisi"})

from comar.service import *

MSG_ERR_APMNOTFOND = {"en": "APM not found.",
                      "tr": "APM bulunamadı.",
                      }

@synchronized
def start():
    import os
    if not os.path.exists("/proc/apm"):
        fail(_(MSG_ERR_APMNOTFOND))

    startService(command="/usr/sbin/apmd",
                 args=config.get("APMD_OPTS", ""),
                 pidfile="/var/run/apmd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/apmd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/apmd.pid")
