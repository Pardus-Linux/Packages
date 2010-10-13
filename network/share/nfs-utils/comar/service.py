# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "NFS Daemon",
                 "tr": "NFS Servisi"
                 })

MSG_ERR_STRTSRVC = {"en": "Unable to start service.",
                    "tr": "Servis başlatılamadı.",
                    }
MSG_ERR_STOPSRVC = {"en": "Unable to stop service.",
                    "tr": "Servis durdurulamadı.",
                    }

def start():
    startDependencies("portmap")
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/rpc.idmapd")
    ret += run("/sbin/start-stop-daemon --start --quiet --exec /sbin/rpc.statd")
    ret += run("/usr/sbin/exportfs -r")
    ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/rpc.nfsd")
    ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/rpc.mountd")
    if ret == 0:
        notify("System.Service", "Changed", (script(), "started"))
    else:
        fail(_(MSG_ERR_STRTSRVC))

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --oknodo --exec /usr/sbin/rpc.mountd")
    ret += run("/sbin/start-stop-daemon --stop --quiet --oknodo --name nfsd --user root --signal 2")
    ret += run("/usr/sbin/exportfs -ua")
    ret += run("/sbin/start-stop-daemon --stop --quiet --exec /sbin/rpc.statd")
    ret += run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/rpc.idmapd")
    call("portmap", "System.Service", "stop")
    if ret == 0:
        notify("System.Service", "Changed", (script(), "stopped"))
    else:
        fail(_(MSG_ERR_STOPSRVC))

def status():
    return isServiceRunning("/var/run/rpc.statd.pid")
