from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "SVN Server",
                 "tr": "SVN Sunucusu"})
serviceConf = "svnserve"

@synchronized
def start():
    startService(command="/usr/bin/svnserve",
                 args="--foreground --daemon %s" % config.get("SVNSERVE_OPTS"),
                 chuid="%s:%s" % (config.get("SVNSERVE_USER"), config.get("SVNSERVE_GROUP")),
                 detach=True,
                 pidfile="/var/run/svnserve.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/svnserve.pid", donotify=True)

def status():
    return isServiceRunning("/var/run/svnserve.pid")
