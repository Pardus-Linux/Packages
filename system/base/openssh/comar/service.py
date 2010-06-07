# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Secure Shell Server",
                 "tr": "Güvenli Kabuk Sunucusu"
                 })

MSG_ERR_NEEDCONF = _({"en": "You need /etc/ssh/sshd_config to run sshd.",
                      "tr": "Sshd'yi çalıştırabilmek için /etc/ssh/sshd_config'e ihtiyaç var.",
                      })

def check_config():
    import os
    if not os.path.exists("/etc/ssh/sshd_config"):
        fail(MSG_ERR_NEEDCONF)
    if not os.path.exists("/etc/ssh/ssh_host_key"):
        run("/usr/bin/ssh-keygen", "-t", "rsa1", "-b", "1024",
            "-f", "/etc/ssh/ssh_host_key", "-N", "")
    if not os.path.exists("/etc/ssh/ssh_host_dsa_key"):
        run("/usr/bin/ssh-keygen", "-d", "-f",
            "/etc/ssh/ssh_host_dsa_key", "-N", "")
    if not os.path.exists("/etc/ssh/ssh_host_rsa_key"):
        run("/usr/bin/ssh-keygen", "-t", "rsa",
            "-f", "/etc/ssh/ssh_host_rsa_key", "-N", "")

@synchronized
def start():
    check_config()
    startService(command="/usr/sbin/sshd",
                 pidfile="/var/run/sshd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/sshd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/sshd.pid")
