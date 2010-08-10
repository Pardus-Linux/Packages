# -*- coding: utf-8 -*-
serviceType="server"
serviceDesc = _({"en": "PostgreSQL Database Server",
                 "tr": "PostgreSQL Veritabanı Sunucusu"})
serviceConf = "postgresql"

MSG_ERR_PGSQLNOTINST = _({"en": "PostgreSQL is not installed.",
                          "tr": "PostgreSQL kurulu değil.",
                          })

from comar.service import *

def check_postgresql():
    import os
    if not os.path.exists(config.get("PGDATA", "/var/lib/postgresql/data")):
        fail(MSG_ERR_PGSQLNOTINST)

pidfile = "%s/postmaster.pid" % config.get("PGDATA", "/var/lib/postgresql/data")

@synchronized
def start():
    check_postgresql()
    startService(command="/usr/bin/pg_ctl",
                 args=["start", "-D", config.get("PGDATA", "/var/lib/postgresql/data"), "-l", config.get("PGLOG", "/var/lib/postgresql/data/postgresql.log"), "-o", config.get("PGOPTS", "")],
                 pidfile=pidfile,
                 chuid=config.get("PGUSER", "postgres"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/pg_ctl",
                args=["stop", "-D", config.get("PGDATA", "/var/lib/postgresql/data"), "-s", "-m", "fast"],
                chuid=config.get("PGUSER", "postgres"),
                donotify=True)

def reload():
    stopService(command="/usr/bin/pg_ctl",
                args=["reload", "-D", config.get("PGDATA", "/var/lib/postgresql/data"), "-s"],
                donotify=True)

def status():
    return isServiceRunning(pidfile)
