#!/usr/bin/python
# -*- coding: utf-8 -*-

MSG_WIRELESS = {
    "en": "Wireless",
    "tr": "Kablosuz Ağlar",
    "fr": "Réseaux sans-fil",
    "es": "Redes inalambricos",
    "sv": "Trådlösa nätverk",
    "de": "Drahtlose Netzwerke",
    "nl": "Draadloos netwerk",
}

MSG_DHCP_FAILED = {
    "en": "Could not acquire an address.",
    "tr": "Adres alınamadı.",
    "fr": "Impossible d'obtenir une adresse.",
    "es": "No posible obtener dirección.",
    "sv": "Kunde inte erhålla adress.",
    "de": "Konnte keine Adresse beziehen.",
    "nl": "Ophalen van adres is mislukt.",
}

MSG_NO_DEVICE = {
    "en": "Device is not plugged.",
    "tr": "Aygıt takılı değil.",
    "fr": "Le matériel est débranché.",
    "es": "Dispositivo no esté conectado.",
    "sv": "Enheten är inte ansluten.",
    "de": "Gerät ist nicht angeschlossen.",
    "nl": "Apparaat is niet aangesloten.",
}

MSG_NO_DRIVER = {
    "en": "Device driver is missing. You may need to install device firmware.",
    "tr": "Aygıt sürücüsü bulunamadı. Aygıta ait bellenim paketini kurmanız gerekebilir.",
    "fr": "Il n'y a pas de pilote installé pour ce matériel.",
    "es": "Falta el controlador del dispositivo. Se requiere instalar el firmware del dispositivo.",
    "de": "Gerätetreiber fehlt. Bitte entsprechenden Firmwaretreiber installieren.",
    "nl": "Stuurprogramma voor apparaat is niet aanwezig. Eventueel firmware installeren.",
}

MSG_NO_SUPPLICANT = {
    "en": "WPA supplicant not found.",
    "tr": "WPA aracısı bulunamadı.",
    "fr": "Impossible de trouver WPA supplicant.",
    "es": "WPA supplicant no encontrado.",
    "sv": "Kunde inte hitta WPA supplikant.",
    "de": "WPA supplicant nicht gefunden.",
    "nl": "WPA-supplicant niet gevonden.",
}

MSG_NO_SUPPLICANT_SERVICE = {
    "en": "Unable to start WPA supplicant service.",
    "tr": "WPA aracı servisi başlatılamadı.",
    "fr": "Impossible de lancer le service WPA supplicant.",
    "es": "No posible iniciar el servicio WPA supplicant",
    "de": "WPA supplicant service konnte nicht gestartet werden.",
    "nl": "Dienst voor WPA-supplicant kan niet gestart worden.",
}

MSG_WPA_FAILED = {
    "en": "Authentication failed.",
    "tr": "Kimlik doğrulama başarısız oldu.",
    "fr": "Échec d'authentification.",
    "es": "Autenticación fallada.",
    "sv": "Autentiseringen misslyckades.",
    "de": "Authentifizierung fehlgeschlagen.",
    "nl": "Authenticatie is mislukt",
}

AUTH_WPA_PSK = {
    "en": "WPA Pre-shared Key",
    "tr": "WPA Ortak Anahtar",
    "fr": "Clef WPA pre-shared",
    "es": "Clave compartida WPA",
    "sv": "Utdelad WPA-nyckel",
    "de": "WPA Pre-Shared Key",
    "nl": "Sleutel voor WPA Pre-Shared",
}

AUTH_WEP_DYNAMIC = {
    "en": "Dynamic WEP (802.1x)",
    "tr": "Dinamik WEP (802.1x)",
    "fr": "WEP dynamique (802.1x)",
    "es": "WEP dinámico (802.1x)",
    "sv": "Dynamisk WEP (802.1x)",
    "de": "Dynamische WEP (802.1x)",
    "nl": "Dynamische WEP (802.1x)",
}

PARAM_PASSWORD = {
    "en": "Password",
    "tr": "Parola",
    "fr": "Mot de passe",
    "nl": "Wachtwoord",
}

PARAM_USERNAME = {
    "en": "Username",
    "tr": "Kullanıcı Adı",
    "fr": "Nom d'utilisateur",
    "es": "Contraseña",
    "de": "Passwort",
    "nl": "Gebruikernaam",
}

PARAM_CLIENT_CERT = {
    "en": "Client Certificate",
    "tr": "İstemci Sertifikası",
    "fr": "Certificat du client",
    "es": "Certificado del cliente",
    "de": "Zertifikat des Clients",
    "nl": "Client-certificaat",
}

PARAM_CA_CERT = {
    "en": "Authority Certificate",
    "tr": "Otorite Sertifikası",
    "fr": "Certificat d'autorité",
    "nl": "Authority-certificaat",
}

PARAM_KEY_FILE = {
    "en": "Key File",
    "tr": "Anahtar Dosyası",
    "fr": "Fichier clef",
    "es": "Archivo de Clave",
    "de": "Datei mit Schlüssel",
    "nl": "Sleutelbestand",
}

DEVICE_MANAGED = {
    "en": "Normal",
    "tr": "Normal",
    "fr": "Normal",
    "es": "Normal",
    "de": "Normal",
    "nl": "Normaal",
}

DEVICE_ADHOC = {
    "en": "Ad-Hoc",
    "tr": "Ad-Hoc",
    "fr": "Ad-hoc",
    "nl": "Ad-Hoc",
}

REMOTE_LABEL = {
    "en": "ESSID",
    "tr": "ESSID",
    "fr": "ESSID",
    "nl": "ESSID",
}

import os
import re
import socket
import array
import struct
import fcntl
import subprocess

from pardus import netutils
from comar.network import Profile, listProfiles, AccessPoint, stopSameDevice, registerNameServers, unregisterNameServers, callScript, plugCheck, plugService

# From </usr/include/wireless.h>
SIOCSIWMODE = 0x8B06    # set the operation mode
SIOCGIWMODE = 0x8B07    # get operation mode
SIOCGIWRATE = 0x8B21    # get default bit rate
SIOCSIWESSID = 0x8B1A   # set essid
SIOCGIWESSID = 0x8B1B   # get essid


class Wireless:
    modes = ['auto', 'adhoc', 'managed', 'master', 'repeat', 'second', 'monitor']

    def __init__(self, ifc):
        self.sock = None
        self.ifc = ifc
        self.ssid = None

    def _call(self, func, arg = None):
        if arg is None:
            data = (self.ifc.name + '\0' * 32)[:32]
        else:
            data = (self.ifc.name + '\0' * 16)[:16] + arg
        try:
            result = self.ifc.ioctl(func, data)
        except IOError:
            return None
        return result

    def getSSID(self):
        buffer = array.array('c', '\0' * 16)
        addr, length = buffer.buffer_info()
        arg = struct.pack('Pi', addr, length)
        self._call(SIOCGIWESSID, arg)
        return buffer.tostring().strip('\x00')

    def setSSID(self, ssid):
        self.ssid = ssid
        point = AccessPoint(ssid)
        buffer = array.array('c', point.ssid + '\x00')
        addr, length = buffer.buffer_info()
        arg = struct.pack("lHH", addr, length, 1)
        self._call(SIOCSIWESSID, arg)
        if self.getSSID() is point.ssid:
            return True
        else:
            return False

    def scanSSID(self):
        ifc = self.ifc
        if not ifc.isUp():
            # Some drivers cant do the scan while interface is down, doh :(
            ifc.setAddress("0.0.0.0")
            if ifc.up() == None:
                fail(_(MSG_NO_DRIVER))
        cmd = subprocess.Popen(["/usr/sbin/iwlist", ifc.name, "scan"], stdout=subprocess.PIPE)
        data = cmd.communicate()[0]
        points = []
        point = None
        for line in data.split("\n"):
            line = line.lstrip()
            if line.startswith("Cell "):
                if point != None:
                    points.append(point)
                point = AccessPoint()
            if "ESSID:" in line:
                i = line.find('"') + 1
                j = line.find('"', i)
                point.ssid = line[i:j]
            if "Protocol:" in line:
                point.protocol = line.split("Protocol:")[1]
            if "Encryption key:" in line:
                mode = line.split("Encryption key:")[1]
                if mode == "on":
                    point.encryption = "wepascii"
            if "IE:" in line:
                ie = line.split("IE:")[1].strip()
                if "WPA" in ie or "WPA2" in ie:
                    point.encryption = "wpa-psk"
            if "Authentication Suites" in line:
                point.auth_suit = line.split(":")[1].strip()
                if "802.1x" in point.auth_suit:
                    point.encryption = "802.1x"
            if "Mode:" in line:
                point.mode = line.split("Mode:")[1]
            if "Channel:" in line:
                point.channel = line.split("Channel:")[1]
            if "Address:" in line:
                point.mac = line.split("Address:")[1].strip()
            if "Quality" in line:
                qual = line.split("Quality")[1][1:]
                qual = qual.split(" ")[0]
                if "/" in qual:
                    qual, max = qual.split("/")
                    # normalize to 0-100
                    if max != "100":
                        qual = (float(qual) * 100) / float(max)
                        qual = str(int(qual))
                        point.qual_max = max
                point.qual = qual
        if point != None:
            points.append(point)
        return points

    def getMode(self):
        result = self._call(SIOCGIWMODE)
        mode = struct.unpack("i", result[16:20])[0]
        return self.modes[mode]

    def setMode(self, mode):
        arg = struct.pack("l", self.modes.index(mode))
        self._call(SIOCSIWMODE, arg)
        if self.getMode() is mode:
            return True
        else:
            return False

    def setEncryption(self, mode=None, parameters=None):
        supplicant = True
        try:
            import wpa_supplicant
        except ImportError:
            supplicant = False

        os.system("/usr/sbin/iwconfig %s enc off" % self.ifc.name)

        if supplicant and wpa_supplicant.isWpaServiceUsable():
            wpa_supplicant.disableAuthentication(self.ifc.name)

        # TODO a guessEncryption() function to determine if its wep or wepascii or open (no enc)
        # TODO check returning data from iwconfig, these calls dont work most of the time but we simply pass
        if mode == "wep":
            os.system("/usr/sbin/iwconfig '%s' enc restricted '%s'" % (self.ifc.name, parameters["password"]))
        elif mode == "wepascii":
            os.system("/usr/sbin/iwconfig '%s' enc restricted 's:%s'" % (self.ifc.name, parameters["password"]))
        elif mode == "wpa-psk":
            if not supplicant:
                fail(_(MSG_NO_SUPPLICANT))
            if not wpa_supplicant.startWpaService():
                fail(_(MSG_NO_SUPPLICANT_SERVICE))
            try:
                ret = wpa_supplicant.setWpaAuthentication(self.ifc.name, self.ssid, parameters["password"])
            except:
                return
            if not ret:
                fail(_(MSG_WPA_FAILED))
        elif mode == "802.1x":
            pass

    def getBitrate(self, ifname):
        # Note for UI coder, KILO is not 2^10 in wireless tools world
        result = self._call(SIOCGIWRATE)
        size = struct.calcsize('ihbb')
        m, e, i, pad = struct.unpack('ihbb', result[16:16+size])
        if e == 0:
            bitrate =  m
        else:
            bitrate = float(m) * 10**e
        return bitrate

# Network.Link methods

def linkInfo():
    d = {
        "type": "wifi",
        "name": _(MSG_WIRELESS),
        "modes": "device,device_mode,remote,remote_scan,net,auto,auth",
    }
    return d

def authMethods():
    return [
        ("wep", "WEP"),
        ("wepascii", "WEP ASCII"),
        ("wpa-psk", _(AUTH_WPA_PSK)),
        ("802.1x", _(AUTH_WEP_DYNAMIC)),
    ]

def authParameters(mode):
    if mode in ("wep", "wepascii", "wpa-psk"):
        return [
            ("password", _(PARAM_PASSWORD), "pass"),
        ]
    elif mode == "802.1x":
        return [
            ("username", _(PARAM_USERNAME), "text"),
            ("password", _(PARAM_PASSWORD), "pass"),
            ("cert_cli", _(PARAM_CLIENT_CERT), "file"),
            ("cert_ca", _(PARAM_CA_CERT), "file"),
            ("keyfile", _(PARAM_KEY_FILE), "file"),
        ]

def remoteName():
    return _(REMOTE_LABEL)

def deviceModes():
    return [
        ("managed", _(DEVICE_MANAGED)),
        ("adhoc", _(DEVICE_ADHOC)),
    ]

def deviceList():
    iflist = {}
    for ifc in netutils.interfaces():
        if ifc.isWireless():
            uid = ifc.deviceUID()
            info = netutils.deviceName(uid)
            iflist[uid] = info
    return iflist

def scanRemote(device):
    if device:
        ifc = netutils.findInterface(device)
        if ifc:
            wifi = Wireless(ifc)
            points = map(lambda x: x.id(), wifi.scanSSID())
            return points
    return []

def setDevice(name, device):
    profile = Profile(name)
    profile.info["device"] = device
    profile.save()

def setDeviceMode(name, mode):
    profile = Profile(name)
    profile.info["device_mode"] = mode
    profile.save()

def deleteConnection(name):
    profile = Profile(name)
    profile.delete()
    notify("Network.Link", "connectionChanged", ("deleted", name))

def setAddress(name, mode, address, mask, gateway):
    profile = Profile(name)
    profile.info["net_mode"] = mode
    profile.info["net_address"] = address
    profile.info["net_mask"] = mask
    profile.info["net_gateway"] = gateway
    profile.save()

def setRemote(name, remote):
    profile = Profile(name)
    profile.info["remote"] = remote
    profile.save()

def setNameService(name, namemode, nameserver):
    profile = Profile(name)
    profile.info["name_mode"] = namemode
    profile.info["name_server"] = nameserver
    profile.save()

def setAuthMethod(name, method):
    profile = Profile(name)
    profile.info["auth"] = method
    profile.save()

def setAuthParameters(name, key, value):
    profile = Profile(name)
    profile.info["auth_%s" % key] = value
    profile.save()

def getAuthMethod(name):
    profile = Profile(name)
    return profile.info.get("auth", "")

def getAuthParameters(name):
    profile = Profile(name)
    d = {}
    for key in profile.info:
        if key.startswith("auth_"):
            d[key[5:]] = profile.info[key]
    return d

def getState(name):
    profile = Profile(name)
    return profile.info.get("state", "down")

def setState(name, state):
    profile = Profile(name)
    ifname = profile.info["device"].split(":")[-1].split("_")[-1]
    iface = netutils.findInterface(profile.info["device"])
    if state == "unplugged" or not iface:
        # Reset Network Stack
        unregisterNameServers(ifname)
        if state == "down":
            # Save state to profile database
            profile.info["state"] = "down"
            profile.save(no_notify=True)
            # Notify clients
            notify("Network.Link", "stateChanged", (name, "down", ""))
        else:
            # Save state to profile database
            profile.info["state"] = "unplugged"
            profile.save(no_notify=True)
            # Notify clients
            notify("Network.Link", "stateChanged", (name, "unplugged", ""))
        # Run profile script (/etc/network/netlink.d/profilename.down)
        callScript(name, "down")
        return
    # Here we go...
    device_mode = profile.info.get("device_mode", "managed").lower()
    if device_mode == "managed":
        if state == "up":
            # Stop other profiles on same device
            stopSameDevice(name)
            # Notify clients
            notify("Network.Link", "stateChanged", (name, "connecting", ""))
            # Save state to profile database
            profile.info["state"] = "connecting"
            profile.save(no_notify=True)
            # Wifi settings
            wifi = Wireless(iface)
            wifi.setSSID(profile.info["remote"])
            # Set encryption
            try:
                wifi.setEncryption(getAuthMethod(name), getAuthParameters(name))
            except Exception, e:
                # Stop ifplug deamon
                plugService(ifname, "down")
                # Save state to profile database
                profile.info["state"] = "inaccessible %s" % unicode(e)
                profile.save(no_notify=True)
                # Notify clients
                notify("Network.Link", "stateChanged", (name, "inaccessible", unicode(e)))
                fail(unicode(e))
            if profile.info.get("net_mode", "auto") == "auto":
                # Start DHCP client
                ret = iface.startAuto()
                if ret == 0 and iface.isUp():
                    if "net_address" in profile.info or "net_gateway" in profile.info:
                        net_address = profile.info.get("net_address", None)
                        net_mask = profile.info.get("net_mask", "255.255.255.0")
                        net_gateway = profile.info.get("net_gateway", None)
                        if net_address:
                            iface.setAddress(net_address, net_mask)
                            if not net_gateway:
                                gateways = iface.autoGateways()
                                if len(gateways):
                                    net_gateway = gateways[0]
                        if net_gateway:
                            route = netutils.Route()
                            route.setDefault(net_gateway)
                    elif iface.getAddress():
                        net_address = iface.getAddress()[0]
                    else:
                        # Bring device down
                        iface.down()
                        # Save state to profile database
                        profile.info["state"] = "inaccessible %s" % _(MSG_DHCP_FAILED)
                        profile.save(no_notify=True)
                        # Notify clients
                        notify("Network.Link", "stateChanged", (name, "inaccessible", _(MSG_DHCP_FAILED)))
                        return
                    # Set nameservers
                    registerNameServers(profile, iface)
                    # Save state to profile database
                    profile.info["state"] = "up " + net_address
                    profile.save(no_notify=True)
                    # Notify clients
                    notify("Network.Link", "stateChanged", (name, "up", net_address))
                    # Run profile script (/etc/network/netlink.d/profilename.up)
                    callScript(name, "up")
                    # Start ifplug daemon
                    plugService(ifname, "up", wireless=True)
                else:
                    # Bring device down
                    iface.down()
                    # Save state to profile database
                    profile.info["state"] = "inaccessible %s" % _(MSG_DHCP_FAILED)
                    profile.save(no_notify=True)
                    # Notify clients
                    notify("Network.Link", "stateChanged", (name, "inaccessible", _(MSG_DHCP_FAILED)))
            else:
                try:
                    net_address = profile.info["net_address"]
                    net_mask = profile.info["net_mask"]
                except KeyError:
                    return
                # Set address
                iface.setAddress(net_address, net_mask)
                # Bring up interface
                if iface.up() == None:
                    fail(_(MSG_NO_DRIVER))
                # Set default gateway
                net_gateway = profile.info.get("net_gateway", "")
                if net_gateway:
                    route = netutils.Route()
                    route.setDefault(net_gateway)
                # Set nameservers
                registerNameServers(profile, iface)
                # Save state to profile database
                profile.info["state"] = "up " + net_address
                profile.save(no_notify=True)
                # Notify clients
                notify("Network.Link", "stateChanged", (name, "up", net_address))
                # Run profile script (/etc/network/netlink.d/profilename.up)
                callScript(name, "up")
                # Start ifplug deamon
                plugService(ifname, "up")
        elif state == "down":
            if profile.info.get("net_mode", "auto") == "auto":
                iface.stopAuto()
            # Set encryption to none
            wifi = Wireless(iface)
            wifi.setEncryption(None, None)
            # Reset Network Stack
            unregisterNameServers(ifname)
            # Bring device down
            iface.down()
            # Save state to profile database
            profile.info["state"] = "down"
            profile.save(no_notify=True)
            # Notify clients
            notify("Network.Link", "stateChanged", (name, "down", ""))
            # Run profile script (/etc/network/netlink.d/profilename.down)
            callScript(name, "down")
    elif device_mode == "adhoc":
        # TODO: AdHoc support
        pass

def connections():
    return listProfiles()

def connectionInfo(name):
    profile = Profile(name)
    device = profile.info.get("device", "")
    return {
        "name": name,
        "device_id": device,
        "device_name": netutils.deviceName(device),
        "device_mode": profile.info.get("device_mode", "managed"),
        "net_mode": profile.info.get("net_mode", "auto"),
        "net_address": profile.info.get("net_address", ""),
        "net_mask": profile.info.get("net_mask", ""),
        "net_gateway": profile.info.get("net_gateway", ""),
        "remote": profile.info.get("remote", ""),
        "name_mode": profile.info.get("name_mode", "default"),
        "name_server": profile.info.get("name_server", ""),
        "state": profile.info.get("state", "down"),
    }

def kernelEvent(data):
    type, dir = data.split("@", 1)
    if not "/net/" in dir:
        return
    device = dir.split("/net/")[-1]
    new = True

    if type == "add":
        # Get device information
        ifc = netutils.IF(device)
        device_id = ifc.deviceUID()
        if not ifc.isWireless():
            return
        # Notify clients
        notify("Network.Link", "deviceChanged", ("add", "wifi", device_id, netutils.deviceName(device_id)))
        # Bring related connection up
        for pn in listProfiles():
            profile = Profile(pn)
            if profile.info.get("device", None) == device_id:
                new = False
                if profile.info.get("state", "down").startswith("unplugged"):
                    setState(pn, "up")
                    break
        # Notify clients if device has no connections
        if new:
            notify("Network.Link", "deviceChanged", ("new", "wifi", device_id, netutils.deviceName(device_id)))
    elif type == "remove":
        # Bring related connection down
        for pn in listProfiles():
            profile = Profile(pn)
            if profile.info.get("device", "").split(":")[-1].split("_")[-1] == device:
                if profile.info.get("state", "down").startswith("up"):
                    # Stop ifplug daemon
                    plugService(device, "down", wireless=True)
                    setState(pn, "unplugged")
                    break
        # Notify clients
        notify("Network.Link", "deviceChanged", ("removed", "wifi", device, ""))
