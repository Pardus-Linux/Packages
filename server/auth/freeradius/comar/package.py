#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    bins = ['radclient', 'radeapclient', 'radlast', 'radsniff', 'radsqlrelay',\
           'radtest', 'radwho', 'radzap', 'rlm_ippool_tool', 'smbencrypt']

    for i in bins:
        os.system("/bin/chown radiusd:radiusd %s/%s" % ("/usr/bin", i))

    for j in ['checkrad', 'radiusd', 'radwatch', 'rc.radiusd']:
        os.system("/bin/chown radiusd:radiusd %s/%s" % ("/usr/sbin", j))

    os.system("/bin/chown -R radiusd:radiusd /var/log/radius")
    os.system("/bin/chown -R radiusd:radiusd /var/run/radiusd")

    os.system("/bin/chown -R radiusd:radiusd /etc/raddb")
