#!/usr/bin/python

import os
from pardus import netutils as network

action = os.environ.get("ACTION", None)
devpath = os.environ.get("DEVPATH", None)

ifc = network.IF(devpath.split("/")[-1])
if action in ["add", "remove"]:
    os.system('/usr/bin/hav call net_tools Network.Link kernelEvent "%s@%s"' % (action, devpath))
