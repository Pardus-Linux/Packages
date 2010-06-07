#!/usr/bin/python
# -*- coding: utf-8 -*-

MSG_ETHERNET = {
    "en": "Ethernet",
    "tr": "Ethernet Ağları",
    "fr": "Réseaux Ethernet",
    "es": "Redes Ethernet",
    "sv": "Ethernet-nätverk",
    "de": "Ethernet-Netzwerke",
    "nl": "Ophalen van adres is mislukt.",
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

import os
import time
from pardus import netutils
from comar.network import listProfiles, Profile, stopSameDevice, registerNameServers, unregisterNameServers, callScript, plugCheck, plugService

# Network.Link methods

def linkInfo():
    return {
        "type": "net",
        "name": _(MSG_ETHERNET),
        "modes": "device,net,auto",
    }

def authMethods():
    # TODO: Raise an exception here. "auth" mode not supported
    return []

def authParameters(mode):
    # TODO: Raise an exception here. "auth" mode not supported
    return []

def remoteName():
    # TODO: Raise an exception here. "remote" mode not supported
    return ""

def deviceModes():
    # TODO: Raise an exception here. "device_mode" mode not supported
    return []

def deviceList():
    iflist = {}
    for ifc in netutils.interfaces():
        if ifc.isEthernet() and not ifc.isWireless():
            uid = ifc.deviceUID()
            info = netutils.deviceName(uid)
            iflist[uid] = info
    return iflist

def scanRemote(device):
    # TODO: Raise an exception here. "remote_scan" mode not supported
    return []

def setDevice(name, device):
    profile = Profile(name)
    profile.info["device"] = device
    profile.save()

def setDeviceMode(name, mode):
    # TODO: Raise an exception here. "device_mode" mode not supported
    pass

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
    # TODO: Raise an exception here. "remote" mode not supported
    pass

def setNameService(name, namemode, nameserver):
    profile = Profile(name)
    profile.info["name_mode"] = namemode
    profile.info["name_server"] = nameserver
    profile.save()

def setAuthMethod(name, method):
    # TODO: Raise an exception here. "auth" mode not supported
    pass

def setAuthParameters(name, key, value):
    # TODO: Raise an exception here. "auth" mode not supported
    pass

def getAuthMethod(name):
    # TODO: Raise an exception here. "auth" mode not supported
    return ""

def getAuthParameters(name):
    # TODO: Raise an exception here. "auth" mode not supported
    return {}

def getState(name):
    profile = Profile(name)
    return profile.info.get("state", "down")

def setState(name, state):
    profile = Profile(name)
    ifname = profile.info["device"].split(":")[-1].split("_")[-1]
    iface = netutils.findInterface(profile.info["device"])

    def saveState(_state, _msg=""):
        # Save state to profile database
        if _msg:
            profile.info["state"] = _state + " " + _msg
        else:
            profile.info["state"] = _state
        profile.save(no_notify=True)
        # Notify clients
        notify("Network.Link", "stateChanged", (name, _state, _msg))
        # Run profile script
        if _state in ["down", "inaccessible", "unplugged"]:
            callScript(name, "down")
        elif _state in ["up"]:
            callScript(name, "up")

    if iface and state == "up":
        if iface.up() == None:
            fail(_(MSG_NO_DRIVER))
        # Check cable state
        saveState("connecting")
        plug = False
        for i in xrange(10):
            if plugCheck(ifname):
                plug = True
                break
            time.sleep(0.5)
        if not plug:
            saveState("unplugged")
            return
    if state == "unplugged" or not iface:
        # Reset Network Stack
        unregisterNameServers(ifname)
        if state == "down":
            saveState("down")
        else:
            saveState("unplugged")
        return
    # Here we go...
    if state == "up":
        # Stop other profiles on same device
        stopSameDevice(name)
        # Save state
        saveState("connecting")
        # Do whatever you need to do...
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
                    # Save state
                    saveState("inaccessible", _(MSG_DHCP_FAILED))
                    return
                # Set nameservers
                registerNameServers(profile, iface)
                # Save state
                saveState("up", net_address)
                # Start ifplug deamon
                plugService(ifname, "up")
            else:
                # Bring device down
                iface.down()
                # Save state
                saveState("inaccessible", _(MSG_DHCP_FAILED))
        else:
            try:
                net_address = profile.info["net_address"]
                net_mask = profile.info["net_mask"]
            except KeyError:
                return
            # Set address
            iface.setAddress(net_address, net_mask)
            if iface.up() == None:
                fail(_(MSG_NO_DRIVER))
            # Set default gateway
            net_gateway = profile.info.get("net_gateway", "")
            if net_gateway:
                route = netutils.Route()
                route.setDefault(net_gateway)
            # Set nameservers
            registerNameServers(profile, iface)
            # Save state
            saveState("up", net_address)
            # Start ifplug deamon
            plugService(ifname, "up")
    elif state == "down":
        if profile.info.get("net_mode", "auto") == "auto":
            iface.stopAuto()
        # Bring device down
        iface.down()
        # Reset Network Stack
        unregisterNameServers(ifname)
        # Save state
        saveState("down")

def connections():
    return listProfiles()

def connectionInfo(name):
    profile = Profile(name)
    device = profile.info.get("device", "")
    return {
        "name": name,
        "device_id": device,
        "device_name": netutils.deviceName(device),
        "net_mode": profile.info.get("net_mode", "auto"),
        "net_address": profile.info.get("net_address", ""),
        "net_mask": profile.info.get("net_mask", ""),
        "net_gateway": profile.info.get("net_gateway", ""),
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
        if ifc.isWireless():
            return
        # Notify clients
        notify("Network.Link", "deviceChanged", ("add", "net", device_id, netutils.deviceName(device_id)))
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
            notify("Network.Link", "deviceChanged", ("new", "net", device_id, netutils.deviceName(device_id)))
    elif type == "remove":
        # Bring related connection down
        for pn in listProfiles():
            profile = Profile(pn)
            if profile.info.get("device", "").split(":")[-1].split("_")[-1] == device:
                if profile.info.get("state", "down").startswith("up"):
                    # Stop ifplug daemon
                    plugService(device, "down")
                    setState(pn, "unplugged")
                    break
        # Notify clients
        notify("Network.Link", "deviceChanged", ("removed", "net", device, ""))
