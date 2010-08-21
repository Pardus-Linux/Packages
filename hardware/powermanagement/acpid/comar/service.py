# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "ACPI Daemon",
                 "tr": "ACPI Servisi"})
serviceDefault = "on"

@synchronized
def start():
    startService(command="/usr/sbin/acpid",
                 args="-c /etc/acpi/events",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/acpid",
                donotify=True)

def ready():
    import os

    if is_on() == "on" and os.path.exists("/proc/acpi/event"):
        start()

def reload():
    import signal
    stopService(command="/usr/sbin/acpid",
                signal=signal.SIGHUP)

def status():
    return isServiceRunning(command="/usr/sbin/acpid")
