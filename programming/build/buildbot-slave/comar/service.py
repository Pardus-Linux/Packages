from comar.service import *
import os.path
from os import stat
from pwd import getpwuid

serviceType = "local"

serviceDesc = _({"en": "Build/test automation system's slave",
                 "tr": "İnşa etme/test etme otomasyon sistemi istemcisi"})

serviceDefault = "off"

serviceConf="buildslave"

slave_dir = config.get("SLAVE_DIR")
PIDFILE = "%s/buildslave.pid" % slave_dir

MSG_NOSLAVE_ERR = _({"en": "Coluld't find a slave configuration under /var/lib/buildslave. Use \"buildslave create-slave /var/lib/buildslave hostname:port user pass\" to create.",
                        "tr": "/var/lib/buildslave dizini altında bir istemci yapılandırması bulunamadı. \"buildslave create-slave /var/lib/buildslave hostname:port istemci parola\" komutu ile oluşturabilirsiniz.",
                        })

def check_config():
    if not (os.path.exists("%s/buildbot.tac" % slave_dir) and os.path.isfile("%s/buildbot.tac" % slave_dir)):
        fail(MSG_NOSLAVE_ERR)


@synchronized
def start():
    check_config()
    loadEnvironment()
    startService(command="/usr/bin/twistd",
                 args="--no_save \
                       --python=%s/buildbot.tac \
                       --logfile=%s/twistd.log \
                       --pidfile=%s \
                       %s" % (slave_dir, slave_dir, PIDFILE, config.get("TWISTD_OPTS")),
                       chuid=config.get("USERNAME"),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)

