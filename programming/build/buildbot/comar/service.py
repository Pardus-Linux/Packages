from comar.service import *
import os.path
from os import stat
from pwd import getpwuid

serviceType = "local"

serviceDesc = _({"en": "Build/test automation system's master",
                 "tr": "İnşa etme/test etme otomasyon sistemi sunucusu"})

serviceDefault = "off"

serviceConf="buildmaster"

MSG_CONFIG_ERR = _({"en": "Couldn't find a valid configuration file (master.cfg) under directory /var/lib/buildmaster. You can create one from the master.cfg.sample file in this directory or you can install buildbot-doc package to see configuration examples. (You can find buildmaster log in \"/var/lib/buildmaster/twistd.log\")",
                    "tr": "/var/lib/buildmaster dizini altında geçerli bir yapılandırma dosyası (master.cfg) bulunamadı. Bu dizin içerisindeki master.cfg.sample dosyasından ya da buildbot-doc paketi içindeki örneklerden yararlanarak oluşturabilirsiniz. (Buildbot ile ilgili logları \"/var/lib/buildmaster/twistd.log\" dosyasında bulabilirsiniz.)",
                    })

master_dir = config.get("MASTER_DIR")
PIDFILE = "%s/buildmaster.pid" % master_dir

def check_config():
    if not (os.path.exists("%s/buildbot.tac" % master_dir) and os.path.isfile("%s/buildbot.tac" % master_dir)):
        run("/usr/bin/buildbot create-master /var/lib/buildmaster")

    if not os.path.isfile("%s/master.cfg" % master_dir):
        fail(MSG_CONFIG_ERR)

@synchronized
def start():
    check_config()
    startService(command="/usr/bin/twistd",
                 args="--no_save \
                       --python=%s/buildbot.tac \
                       --logfile=%s/twistd.log \
                       --pidfile=%s \
                       %s" % (master_dir, master_dir, PIDFILE, config.get("TWISTD_OPTS")),
                       chuid=config.get("USERNAME"),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)

