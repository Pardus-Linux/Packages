#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "corporate2"

def build():
    autotools.make('-C src CC="%s" LD="%s %s" CFLAGS="%s"' % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    # Setup files in /etc
    pisitools.insinto("/", "etc")

    shelltools.chmod("%s/etc/shadow" % get.installDIR(), 0600)

    shelltools.echo("%s/etc/pardus-release" % get.installDIR(), "Pardus Corporate 2 Alpha")

    # Install some files to /usr/share/baselayout instead of /etc to keep from overwriting the user's settings,
    for f in ("passwd", "shadow", "group", "fstab", "hosts", "ld.so.conf", "resolv.conf", "inittab.live"):
        pisitools.domove("/etc/%s" % f, "/usr/share/baselayout")

    # Install baselayout documentation
    pisitools.doman("man/*.*")

    # Install baselayout utilities
    shelltools.cd("src/")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # Create needed directories !!!
    create_directories()

def kdir(directory, parameters = ""):
    """ local function to create needed directories """
    shelltools.system("install -d %s %s/%s" % (parameters, get.installDIR(), directory))

def create_directories():
    kdir("/boot")
    kdir("/dev")
    # these are done in mudur
    # kdir("/dev/pts")
    # kdir("/dev/shm")

    # Create autostart directory
    kdir("/etc/xdg/autostart")

    kdir("/etc/conf.d")
    kdir("/etc/cron.daily")
    kdir("/etc/cron.hourly")
    kdir("/etc/cron.monthly")
    kdir("/etc/cron.weekly")
    kdir("/etc/env.d")
    kdir("/etc/modules.autoload.d")
    kdir("/etc/modules.d")
    kdir("/etc/opt")
    kdir("/home")
    kdir("/media")
    kdir("/lib")
    kdir("/mnt")
    kdir("/mnt/floppy", "-m 0700")
    kdir("/opt")
    kdir("/var/lock", "-o root -g root -m0755")
    kdir("/proc")
    kdir("/sbin")
    kdir("/sys")
    kdir("/usr")
    kdir("/usr/bin")
    kdir("/usr/include")
    kdir("/usr/include/asm")
    kdir("/usr/include/linux")
    kdir("/usr/lib")
    kdir("/usr/local/bin")
    kdir("/usr/local/games")
    kdir("/usr/local/lib")
    kdir("/usr/local/sbin")
    kdir("/usr/local/share")
    kdir("/usr/local/share/doc")
    kdir("/usr/local/share/man")
    kdir("/usr/local/src")
    kdir("/usr/sbin")
    kdir("/usr/share/doc")
    kdir("/usr/share/info")
    kdir("/usr/share/man")
    kdir("/usr/share/misc")
    kdir("/usr/src")
    kdir("/tmp", "-m 01777")
    kdir("/var")
    kdir("/var/lib/misc")
    kdir("/var/lock/subsys")
    kdir("/var/log/news")
    kdir("/var/run/pardus")
    kdir("/var/spool")
    kdir("/var/state")
    kdir("/var/tmp", "-m 01777")

    # Link /usr/share/autostart to /etc/xdg/autostart
    pisitools.dosym("/etc/xdg/autostart", "/usr/share/autostart")

    # FHS compatibility symlinks stuff
    pisitools.dosym("/var/tmp", "/usr/tmp")
    pisitools.dosym("share/man", "/usr/local/man")

    if get.ARCH() == "x86_64":
        # Hack for binary blobs built on multi-lib systems
        pisitools.dosym("lib", "/lib64")
