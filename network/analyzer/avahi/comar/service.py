from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Avahi ZeroConf Server",
                 "tr": "Avahi ZeroConf Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/avahi-daemon",
                 args="-D",
                 donotify=True)

    startService(command="/usr/sbin/avahi-dnsconfd",
                 args="-D",
                 pidfile="/var/run/avahi-daemon.pid",
                 donotify=False)

@synchronized
def stop():
    stopService(command="/usr/sbin/avahi-dnsconfd",
                args="-k",
                donotify=False)

    stopService(command="/usr/sbin/avahi-daemon",
                args="-k",
                donotify=True)

def reload():
    stopService(command="/usr/sbin/avahi-daemon",
                args="-r",
                donotify=True)

    stopService(command="/usr/sbin/avahi-dnsconfd",
                args="-r",
                donotify=True)

def status():
    return isServiceRunning("/var/run/avahi-daemon/pid")
