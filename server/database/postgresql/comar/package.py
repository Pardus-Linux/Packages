#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R postgres:postgres /var/lib/postgresql")
    os.system("/bin/chmod -R 0700 /var/lib/postgresql/data")
    os.system("/bin/chmod -R 0700 /var/lib/postgresql/backups")

    # On first install...
    if not os.access("/var/lib/postgresql/data/base", os.F_OK):
        os.system("/usr/bin/sudo -u postgres /usr/bin/initdb --pgdata /var/lib/postgresql/data")

