from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Smartlink Modem Manager",
                 "tr": "Smartlink Modem Yöneticisi"})

@synchronized
def start():
    args = ""
    mod = config.get("MODULE", "alsa")

    if mod == "alsa":
        args = "--alsa %s" % config.get("HW_SLOT", "modem:1")
    else:
        os.system("/sbin/modprobe %s" % mod)
        mdev = config.get("MDEV", "")
        if mdev == "":
            mdev = "/dev/%s0" % mod

        if not os.path.exists(mdev):
            os.system("/bin/mknod %s c 242 0" % mdev)

        args = mdev

    startService(command="/usr/sbin/slmodemd",
                 args="--country=%s -g=%s %s %s" % (config.get("COUNTRY", "TURKEY"), config.get("GROUP", "dialout"), config.get("SLMODEM_OPTS", ""), args),
                 nice=int(config.get("NICE", "-6")),
                 pidfile="/var/run/slmodemd.pid",
                 makepid=True,
                 detach=True,
                 donotify=True)

    if config.get("LN_DEV", "") != "":
        try:
            os.symlink(config.get("DEV", "/dev/ttySL0"), config.get("LN_DEV", "/dev/modem"))
        except:
            pass

@synchronized
def stop():
    stopService(pidfile="/var/run/slmodemd.pid",
                donotify=True)

    try:
        os.unlink("/var/run/slmodemd.pid")
        os.unlink(config.get("LN_DEV", "/dev/modem"))
    except:
        pass

def status():
    return isServiceRunning("/var/run/slmodemd.pid")
