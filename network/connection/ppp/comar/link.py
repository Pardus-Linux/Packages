#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

name_msg = {"en": "Dialup network",
            "tr": "Çevirmeli ağ",
            }
remote_name_msg = {"en": "Phone number",
                   "tr": "Telefon numarası",
                   }

MSG_ERR_OPENLCKF = {"en": "Could not open lockfile.",
                    "tr": "Kilit dosyası açılamadı.",
                    }
MSG_ERR_STOPPRCS = {"en": "Could not stop the process.",
                    "tr": "Süreç durdurulamadı.",
                    }
MSG_KILD = {"en": "Killed.",
            "tr": "Sonlandırıldı.",
            }
MSG_ERR_MNGEAUTHFLES = {"en": "Could not manage authentication files.",
                        "tr": "Kimlik doğrulama dosyaları işlenemedi.",
                        }
MSG_ERR_MNGEPPPDPRMS = {"en": "Could not manage pppd parameters.",
                        "tr": "pppd parametreleri işlenemedi.",
                        }
MSG_ERR_MNGECHATSCRP = {"en": "Could not manage chat script.",
                        "tr": "Sohbet betiği işlenemedi.",
                        }
MSG_ERR_NOSUCHCONN = {"en": "No such connection.",
                      "tr": "Böyle bir bağlantı yok.",
                      }
MSG_ERR_NOTSPRT = {"en": "Not supported.",
                   "tr": "Desteklenmiyor.",
                   }
MSG_ERR_UNKNSTTE = {"en": "Unknown state.",
                    "tr": "Durum bilinmiyor.",
                    }
MSG_ERR_DEVCNOTFOUN = {"en": "Device not found.",
                       "tr": "Aygıt bulunamadı.",
                       }

# Silly modem device list :/
# Appearently checking existance of these devices is easiest way to detect modems
modem_devices = (
    # Standart list
    "/dev/modem",
    "/dev/ttyS0",
    "/dev/ttyS1",
    "/dev/ttyS2",
    "/dev/ttyS3",
    "/dev/ttyS4",
    # ISDN
    "/dev/ttyI0",
    "/dev/ttyI1",
    "/dev/ttyI2",
    "/dev/ttyI3",
    # USB
    "/dev/usb/ttyACM0",
    "/dev/usb/ttyACM1",
    "/dev/usb/ttyACM2",
    "/dev/usb/ttyACM3",
    "/dev/usb/ttyUSB0",
    "/dev/usb/ttyUSB1",
    "/dev/usb/ttyUSB2",
    "/dev/usb/ttyUSB3",
    "/dev/ttyACM0",
    "/dev/ttyACM1",
    "/dev/ttyACM2",
    "/dev/ttyACM3",
    "/dev/ttyUSB0",
    "/dev/ttyUSB1",
    "/dev/ttyUSB2",
    "/dev/ttyUSB3",
    # BlueTooth
    "/dev/rfcomm0",
    "/dev/rfcomm1",
    "/dev/rfcomm2",
    "/dev/rfcomm3",
    # IrDA
    "/dev/ircomm0",
    "/dev/ircomm1",
    "/dev/ircomm2",
    "/dev/ircomm3",
    # slmodem
    "/dev/ttySL0",
    "/dev/ttySL1",
    "/dev/ttySL2",
    "/dev/ttySL3",
    # hsfmodem
    "/dev/ttySHSF0",
    "/dev/ttySHSF1",
    "/dev/ttySHSF2",
    "/dev/ttySHSF3",
    # hcfmodem
    "/dev/ttySHCF0",
    "/dev/ttySHCF1",
    "/dev/ttySHCF2",
    "/dev/ttySHCF3",
    # ltmodem
    "/dev/ttyLTM0",
    "/dev/ttyLTM1",
    "/dev/ttyLTM2",
    "/dev/ttyLTM3",
)

import os
import popen2
from signal import SIGTERM

from pardus.csapi import atoi
from pardus import iniutils

# Open connection db
DB = iniutils.iniDB(os.path.join("/etc/network", script()))


class Dialup:
    """ Dialup client functions for Hayes compatible modems, using pppd """

    tmpl_chat = """
TIMEOUT         5
ABORT           '\\nBUSY\\r'
ABORT           '\\nNO ANSWER\\r'
ABORT           '\\nNO CARRIER\\r'
ABORT           '\\nNO DIALTONE\\r'
ABORT           '\\nAccess denied\\r'
ABORT           '\\nInvalid\\r'
ABORT           '\\nVOICE\\r'
ABORT           '\\nRINGING\\r\\n\\r\\nRINGING\\r'
''              \\rAT
'OK-+++\c-OK'   ATH0
TIMEOUT         30
OK              ATL%s
OK              ATDT%s
CONNECT         ''
"""
    
    tmpl_options = """
lock
modem
crtscts
noipdefault
defaultroute
noauth
usehostname
usepeerdns
linkname %s
user %s
%s
"""

    def silentUnlink(self, path):
        """ Try to unlink a file, if exists """

        try:
            os.unlink(path)
        except:
            pass

    def capture(self, cmd):
        """ Run a command and capture the output """

        out = []
        a = popen2.Popen4(cmd)
        while 1:
            b = a.fromchild.readline()
            if b == None or b == "":
                break
            out.append(b)
        return (a.wait(), out)

    def sendCmd(self, cmd, dev):
        """ Send commands to dev """

        return result

    def isModem(self, dev):
        """ Check if dev is a modem """
        
        return True

    def getDNS(self):
        """ Try to get DNS server adress provided by remote peer """

        list = []
        try:
            f = file("/etc/ppp/resolv.conf", "r")
            for line in f.readlines():
                if line.strip().startswith("nameserver"):
                    list.append(line[line.find("nameserver") + 10:].rstrip('\n').strip())
            f.close()
        except IOError:
            return None

        return list

    def createOptions(self, dev, user, speed):
        """ Create options file for the desired device """

        self.silentUnlink("/etc/ppp/options." + dev)
        try:
            f = open("/etc/ppp/options." + dev, "w")
            f.write(self.tmpl_options % (dev, user, speed))
            f.close()
        except:
            return True

        return None

    def createChatscript(self, dev, phone, vol):
        """ Create a script to have a chat with the modem in the frame of respect and love """

        self.silentUnlink("/etc/ppp/chatscript." + dev)
        try:
            f = open("/etc/ppp/chatscript." + dev, "w")
            f.write(self.tmpl_chat % (vol, phone))
            f.close()
        except:
            return True

        return None


    def createSecrets(self, user, pwd):
        """ Create authentication files """

        try:
            # Ugly way to clean up secrets and recreate
            self.silentUnlink("/etc/ppp/pap-secrets")
            self.silentUnlink("/etc/ppp/chap-secrets")
            f = os.open("/etc/ppp/pap-secrets", os.O_CREAT, 0600)
            os.close(f)
            os.symlink("/etc/ppp/pap-secrets", "/etc/ppp/chap-secrets")
        except:
            return True
            
        f = open("/etc/ppp/pap-secrets", "w")
        data = "\"%s\" * \"%s\"\n" % (user, pwd)
        f.write(data)
        f.close()

        return None

    def stopPPPD(self, dev):
        """ Stop the connection and hangup the modem """

        try:
            f = open("/var/lock/LCK.." + dev, "r")
            pid = atoi(f.readline())
            f.close()
        except:
            return _(MSG_ERR_OPENLCKF)

        try:
            os.kill(pid, SIGTERM)
        except OSError:
            return _(MSG_ERR_STOPPRCS)

        return _(MSG_KILD)

    def runPPPD(self, dev):
        """ Run the PPP daemon """

        # PPPD does some isatty and ttyname checks, so we shall satisfy it for symlinks and softmodems
        cmd = "/usr/sbin/pppd /dev/" + dev + " connect '/usr/sbin/chat -V -v -f /etc/ppp/chatscript." + dev + "'"
        i, output = self.capture(cmd)

        return output

    def dial(self, phone, user, pwd, speed, vol, modem = "modem"):
        """ Dial a server and try to login """
    
        dev = modem.lstrip("/dev/")

        if self.createSecrets(user, pwd) is True:
            return _(MSG_ERR_MNGEAUTHFLES)

        if self.createOptions(dev, user, speed) is True:
            return _(MSG_ERR_MNGEPPPDPRMS)

        if self.createChatscript(dev, phone, vol) is True:
            return _(MSG_ERR_MNGECHATSCRP)

        output = self.runPPPD(dev)
        return output


def _device_dev(uid):
    return uid[uid.find(":") + 1:]

def _device_info(uid):
    return uid[uid.find(":") + 1:]

def _get(dict, key, default):
    val = default
    if dict and dict.has_key(key):
        val = dict[key]
    return val


class Dev:
    def __init__(self, name, want=False):
        dict = DB.getDB(name)
        if want:
            if not dict:
                fail(_(MSG_ERR_NOSUCHCONN))
        self.uid = _get(dict, "device", None)
        self.name = name
        self.dev = None
        if self.uid:
            self.dev = _device_dev(self.uid)
        self.state = _get(dict, "state", "down")
        self.remote = _get(dict, "remote", None)
        self.authmode = _get(dict, "authmode", "none")
        self.user = _get(dict, "user", "")
        self.password = _get(dict, "password", "")
    
    def up(self):
        dial = Dialup()
        
        if self.remote and self.user and self.password and self.dev:
            notify("Net.Link", "stateChanged", (self.name, "connecting"))
            
            dial.dial(self.remote, self.user, self.password, "115200", "1", self.dev)
            
            d = DB.getDB(self.name)
            d["state"] = "up"
            DB.setDB(self.name, d)
            notify("Net.Link", "stateChanged", (self.name, "up"))
    
    def down(self):
        dial = Dialup()
        dial.stopPPPD(self.dev)
        d = DB.getDB(self.name)
        d["state"] = "down"
        DB.setDB(self.name, d)
        notify("Net.Link", "stateChanged", (self.name, "down"))


#

def linkInfo():
    d = {
        "type": "dialup",
        "name": _(name_msg),
        "modes": "device,remote,auth",
        "auth_modes": "login,login,Login",
        "remote_name": _(remote_name_msg),
    }
    return d

def deviceList():
    iflist = {}
    for dev in modem_devices:
        if os.path.exists(dev):
            iflist["modem:%s" % dev] =_device_info(dev)
    return iflist

def scanRemote():
    fail(_(MSG_ERR_NOTSPRT))

def setConnection(name, device):
    d = DB.getDB(name)
    changed = "device" in d
    d["device"] = device
    DB.setDB(name, d)
    if changed:
        notify("Net.Link", "connectionChanged", ("configured", name))
    else:
        notify("Net.Link", "connectionChanged", ("added", name))

def deleteConnection(name=None):
    dev = Dev(name)
    if dev.dev and dev.state == "up":
        dev.down()
    DB.remDB(name)
    notify("Net.Link", "connectionChanged", ("deleted", name))

def setAddress(name=None, mode=None, address=None, mask=None, gateway=None):
    fail(_(MSG_ERR_NOTSPRT))

def setRemote(name, remote, apmac):
    d = DB.getDB(name)
    d["remote"] = remote
    d["apmac"] = apmac
    DB.setDB(name, d)
    notify("Net.Link", "connectionChanged", ("configured", name))

def setAuthentication(name, authmode, user, password, auth="", anon="", phase2="", clicert="", cacert="", pkey="", pkeypass=""):
    d = DB.getDB(name)
    d["authmode"] = authmode
    d["user"] = user
    d["password"] = password
    DB.setDB(name, d)
    notify("Net.Link", "connectionChanged", ("configured", name))

def getState(name):
    d = DB.getDB(name)
    return d.get("state", "down")

def setState(name, state):
    dev = Dev(name)
    if state != "up" and state != "down":
        fail(_(MSG_ERR_UNKNSTTE))
    
    if not dev.dev:
        fail(_(MSG_ERR_DEVCNOTFOUN))
    
    if state == "up":
        dev.up()
    else:
        if dev.state == "up":
            dev.down()

def connections():
    return DB.listDB()

def connectionInfo(name=None):
    dev = Dev(name, True)
    d = {}
    d["name"] = name
    if dev.uid:
        d["device_id"] = dev.uid
        d["device_name"] = _device_info(dev.uid)
    if dev.remote:
        d["remote"] = dev.remote
    # FIXME:
    d["state"] = dev.state
    return d

def getAuthentication(name):
    dev = Dev(name)
    return (dev.authmode, dev.user, dev.password, "", "", "", "", "", "", "", "")
