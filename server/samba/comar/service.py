serviceType = "server"
serviceDesc = _({"en": "SMB Network Sharing",
                 "tr": "SMB Ağ Paylaşımı"})

from comar.service import *

@synchronized
def start():
    startService(command="/usr/sbin/smbd",
                 args="-D",
                 donotify=True)

    startService(command="/usr/sbin/nmbd",
                 args="-D")

    if config.get("winbind", "no") == "yes":
        startService(command="/usr/sbin/winbindd",
                     args="-D")

@synchronized
def stop():
    stopService(pidfile="/var/run/samba/winbindd.pid")
    stopService(pidfile="/var/run/samba/nmbd.pid")
    stopService(pidfile="/var/run/samba/smbd.pid",
                donotify=True)

def reload():
    import signal
    stopService(pidfile="/var/run/samba/winbindd.pid",
                signalno=signal.SIGHUP)
    stopService(pidfile="/var/run/samba/nmbd.pid",
                signalno=signal.SIGHUP)
    stopService(pidfile="/var/run/samba/smbd.pid",
                signalno=signal.SIGHUP)

def status():
    result = isServiceRunning("/var/run/samba/smbd.pid") and isServiceRunning("/var/run/samba/nmbd.pid")
    if config.get("winbind", "no") == "yes":
        result = result and isServiceRunning("/var/run/samba/winbindd.pid")
    return result
