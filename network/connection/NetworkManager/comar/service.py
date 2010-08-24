# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Network Manager",
                 "tr": "Ağ Yöneticisi Hizmeti"})
serviceDefault = "conditional"

MSG_BACKEND_WARNING = _({
                        "en" : "NetworkManager is not the default backend. You can change the backend from /etc/conf.d/NetworkManager.",
                        "tr" : "NetworkManager öntanımlı ağ arkayüzü değil. /etc/conf.d/NetworkManager dosyasından arkayüzü değiştirebilirsiniz."
                        })

PIDFILE="/var/run/NetworkManager/NetworkManager.pid"
USETHIS=eval(config.get("DEFAULT", "False"))

@synchronized
def start():
    if not USETHIS:
        fail(MSG_BACKEND_WARNING)

    startService(command="/usr/sbin/NetworkManager",
                 args="--pid-file=%s" % PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def ready():
    if not USETHIS:
        fail(MSG_BACKEND_WARNING)
    else:
        start()

def status():
    return isServiceRunning(pidfile=PIDFILE)
