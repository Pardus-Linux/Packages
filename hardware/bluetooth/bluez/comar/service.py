from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Bluetooth Service",
                 "tr": "Bluetooth Hizmeti"})
serviceDefault = "on"

@synchronized
def start():
    # Work-around udev bug, bluetoothd wasn't getting enabled on coldplug
    run("/sbin/udevadm trigger --subsystem-match=bluetooth")

@synchronized
def stop():
    pass

def status():
    return isServiceRunning(command="/usr/sbin/bluetoothd")
