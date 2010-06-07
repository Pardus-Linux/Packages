#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "DNS Cache Service",
                 "tr": "DNS Önbellekleme Servisi"})

DNSMASQMESSAGE = "# This line was added by dnsmasq package"
DNSMASQNAMESERVER = "nameserver 127.0.0.1"

def addLocalNameServerToResolvConf():
    dnslist = []
    for line in file("/etc/resolv.conf"):
        dnslist.append(line)
        line = line.strip()
        if line.startswith(DNSMASQNAMESERVER):
            return

    dnslist.insert(0, "%s\n" % DNSMASQMESSAGE)
    dnslist.insert(1, "%s\n" % DNSMASQNAMESERVER)

    f = file("/etc/resolv.conf", "w")
    try:
        for dns in dnslist:
            f.write(dns)
    finally:
        f.close()

def removeLocalNameServerFromResolvConf():
    dnslist = []
    for line in file("/etc/resolv.conf"):
        strippedLine = line.strip()
        if strippedLine.startswith(DNSMASQMESSAGE):
            continue
        if strippedLine.startswith(DNSMASQNAMESERVER):
            continue
        dnslist.append(line)

    f = file("/etc/resolv.conf", "w")
    try:
        for dns in dnslist:
            f.write(dns)
    finally:
        f.close()

@synchronized
def start():
    addLocalNameServerToResolvConf()
    startService(command="/usr/sbin/dnsmasq",
                 args="--enable-dbus",
                 pidfile="/var/run/dnsmasq.pid",
                 donotify=True)

@synchronized
def stop():
    removeLocalNameServerFromResolvConf()
    stopService(pidfile="/var/run/dnsmasq.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/dnsmasq.pid")
