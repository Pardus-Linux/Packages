#!/usr/bin/python

import os
import time

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R mysql:mysql /var/lib/mysql")
    os.system("/bin/chmod -R 0750 /var/lib/mysql")

    os.system("/bin/chown -R mysql:mysql /var/log/mysql")
    os.system("/bin/chmod 0750 /var/log/mysql")
    os.system("/bin/chmod -R 0660 /var/log/mysql/*")

    os.system("/bin/chown -R mysql:mysql /var/run/mysqld")
    os.system("/bin/chmod -R 0755 /var/run/mysqld")

    # On first install...
    if not os.access("/var/lib/mysql/mysql", os.F_OK):
        os.system("sudo -u mysql /usr/bin/mysql_install_db")

        # Run MySQL
        os.system("/usr/sbin/mysqld --user=mysql \
                                    --skip-grant-tables \
                                    --basedir=/usr \
                                    --datadir=/var/lib/mysql \
                                    --skip-innodb \
                                    --max_allowed_packet=8M \
                                    --net_buffer_length=16K \
                                    --socket=/var/run/mysqld/mysqld.sock \
                                    --pid-file=/var/run/mysqld/mysqld.pid &")


        # Sleep for a while
        time.sleep(2)

        # Delete empty user
        sql = "DELETE FROM mysql.user WHERE USER=''"
        os.system("/usr/bin/mysql --socket=/var/run/mysqld/mysqld.sock \
                                 -hlocalhost \
                                 -e \"%s\"" % sql)

        # Generate timezones
        os.system("/usr/bin/mysql_tzinfo_to_sql /usr/share/zoneinfo > /tmp/pardus.sql")

        # Generate help tables
        os.system("/bin/cat /usr/share/mysql/fill_help_tables.sql >> /tmp/pardus.sql")

        # Load generated SQL script
        os.system('/usr/bin/mysql --socket=/var/run/mysqld/mysqld.sock \
                                  -hlocalhost \
                                  -uroot \
                                  mysql < %s' % '/tmp/pardus.sql')

        # Stop MySQL
        os.kill(int(open("/var/run/mysqld/mysqld.pid", "r").read().strip()), 15)

        # Remove temporary SQL script
        os.unlink("/tmp/pardus.sql")
