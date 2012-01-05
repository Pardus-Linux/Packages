#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

def migrate_hostname():
    old_location = "/etc/env.d/01hostname"
    new_location = "/etc/hostname"
    if not os.path.exists(new_location):
        hostname = open(old_location, "r").read().strip().split("HOSTNAME=")[-1].replace('"', '')
        with open(new_location, "w") as filedata:
            filedata.write("%s\n" % hostname)

def migrate_locale():
    old_location = "/etc/env.d/03locale"
    new_location = "/etc/locale.conf"
    lang = "C"
    if not os.path.exists(new_location):
        with open(old_location, "r") as filedata:
            for line in filedata.readlines():
                if "LANG=" in line:
                    lang = line.split("LANG=")[-1].replace('"', '').rstrip("\n")
                    break
        with open(new_location, "w") as filedata:
            filedata.write("LANG=%s\n" % lang)

def migrate_vconsole_conf():
    old_location = "/etc/mudur/keymap"
    new_location = "/etc/vconsole.conf"

    if not os.path.exists(new_location) \
        and os.path.exists(old_location):
        keymap = open(old_location, "r").read().strip()

        if keymap:
            open(new_location, "w").write("KEYMAP=%s\nFONT=latarcyrheb-sun16" % keymap)

def migrate_modules_autoload_d():
    old_location = "/etc/modules.autoload.d"
    new_location = "/etc/modules.d"

    def generate_new_conf(modname):
        with open(os.path.join(new_location, "%s.conf" % modname), "w") as filedata:
            filedata.write("# Load %s kernel module at boot\n%s\n" % (modname, modname))

    # Look for each file for backward compatibility
    for conf in glob.glob("%s/*" % old_location):
        with open(conf, "r") as filedata:
            for line in filedata.readlines():
                if not line.startswith("#") and line.strip():
                    generate_new_conf(line.strip())


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Generate machine-id
    os.system("/bin/systemd-machine-id-setup &> /dev/null")

    # Re-execute daemon
    os.system("/bin/systemctl daemon-reexec &> /dev/null")

    # Make sure pam_systemd is enabled

    # Do the migrations
    migrate_hostname()
    migrate_locale()
    migrate_vconsole_conf()
    # FIXME: We can do this is modules-init-tools
    # migrate_modules_autoload_d()


if __name__ == "__main__":
    migrate_hostname()
    migrate_locale()
    migrate_modules_autoload_d()
