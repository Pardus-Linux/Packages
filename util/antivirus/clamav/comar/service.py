# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Antivirüs Servisi"})

@synchronized
def start():
    #if config.get("DAZUKO_SUPPORT", "no") == "yes":
    #            call("System.Service.start", "dazuko")

    startService(command="/usr/sbin/clamd",
            chuid="clamav",
            pidfile="/var/run/clamav/clamd.pid",
            donotify=False)
    startService(command="/usr/bin/freshclam",
            args="-d --pid=/var/run/clamav/freshclam.pid",
            chuid="clamav",
            pidfile="/var/run/clamav/freshclam.pid",
            donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/clamd",
                        donotify=True)
    time.sleep(4)
    stopService(command="/usr/bin/freshclam",
                        donotify=True)
    #if config.get("DAZUKO_SUPPORT", "no") == "yes":
    #    call("System.Service.stop", "dazuko")

def status():
    return isServiceRunning("/var/run/clamav/clamd.pid") and isServiceRunning("/var/run/clamav/freshclam.pid")
