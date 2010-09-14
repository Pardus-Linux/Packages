# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "DHCPv6 Daemon",
                 "tr": "DHCPv6 Servisi"})
serviceConf = "dhcpd6"

pidfile = "/var/run/dhcpd6.pid"

@synchronized
def start():
    startService(command="/usr/sbin/dhcpd",
                 args="%s %s" % (config.get("DHCPD_ARGS", ""), config.get("INTERFACES", "")),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/dhcpd",
                pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
