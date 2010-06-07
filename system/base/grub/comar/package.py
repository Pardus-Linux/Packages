#!/usr/bin/python

import os
import shutil
import glob

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    exists = os.path.exists

    stage2src = "/lib/grub/i386-pc/stage2"
    stage2target = "/boot/grub/stage2"

    egrepregexp = "'^[[:space:]]*(#|$|default|fallback|initrd|password|splashimage|timeout|title|gfxmenu|background|configfile)'"

    if not exists("/boot/grub"):
        os.makedirs("/boot/grub")

    if not exists("/boot/grub/grub.conf") and exists("/boot/grub/menu.lst"):
        shutil.move("/boot/grub/menu.lst", "/boot/grub/grub.conf")

    if not os.path.lexists("/boot/grub/menu.lst"):
        os.symlink("grub.conf", "/boot/grub/menu.lst")

    if exists("/boot/grub/stage2"):
        shutil.move("/boot/grub/stage2", "/boot/grub/stage2.old")

    # "Copying files from /lib/grub and /usr/lib/grub to /boot"
    fnlist = glob.glob("/lib/grub/*/*")

    for x in fnlist:
        if os.path.isfile(x):
            if "stage1" in x or "eltorito" in x:
                fname = os.path.basename(x)
                newpath = os.path.join("/boot/grub", fname)
                shutil.copyfile(x, newpath)

    os.system("dd if=%s of=%s bs=256k" % (stage2src, stage2target))
    os.system("sync")

    if exists("/boot/grub/grub.conf"):
        cmd = "/bin/egrep -v %s /boot/grub/grub.conf|/sbin/grub --batch --device-map=/boot/grub/device.map > /dev/null 2>&1" % egrepregexp
        os.system(cmd)

