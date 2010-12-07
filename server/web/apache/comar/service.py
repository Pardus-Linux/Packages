from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Apache Web Server",
                 "tr": "Apache Web Sunucusu"})

serviceConf = "apache2"

PIDFILE = "/var/run/apache2.pid"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/sbin/apache2",
                 args="-d /usr/lib/apache2/ -f /etc/apache2/httpd.conf %s -k start"  % config.get("APACHE2_OPTS", ""),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/apache2",
                args="-d /usr/lib/apache2/ -f /etc/apache2/httpd.conf %s -k stop"  % config.get("APACHE2_OPTS", ""),
                donotify=True)

def reload():
    stopService(command="/usr/sbin/apache2",
                args="-d /usr/lib/apache2/ -f /etc/apache2/httpd.conf %s -k graceful"  % config.get("APACHE2_OPTS", ""))

def status():
    return isServiceRunning(PIDFILE)
