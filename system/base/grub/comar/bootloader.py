#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import shutil

from pardus.grubutils import grubCommand, grubEntry, grubConf
from pardus.diskutils import linuxAddress, grubAddress, getDeviceByUUID, parseLinuxDevice, getRoot

# Make pychecker happy
try:
    x = _
    del x
except NameError:
    fail = notify = _ = lambda x: x

# Grub menu items
MSG_OLD_KERNELS = "otheroptions"
MSG_MAIN_MENU = "mainmenu"

# l10n

FAIL_NOENTRY = _({
    "en": "No such entry.",
    "tr": "Böyle bir kayıt bulunmuyor.",
    "fr": "Il n'existe aucune entrée de ce nom-là.",
    "es": "Entrada no exise.",
    "de": "Dieser Eintrag existiert nicht.",
})

FAIL_NOPARDUSENTRY = _({
    "en": "There should be at least one Pardus kernel entry.",
    "tr": "En az bir Pardus çekirdek girsisi tanımlı olmalı.",
    "fr": "Il devrait y avoir au moins une entrée pour Pardus",
    "es": "Debería haber al menos una entrada con un kernel de Pardus.",
    "de": "Es sollte mindestens einen Eintrag mit einem Pardus-Kernel geben.",
})

FAIL_NODEVICE = _({
    "en": "No such device: '%s'",
    "tr": "Böyle bir aygıt yok: '%s'",
    "fr": "Matériel introuvable: '%s'",
    "es": "No hay dispositivo: '%s'",
    "de": "Gerät nicht vorhanden : '%s'",
})

FAIL_NOSYSTEM = _({
    "en": "No such system.",
    "tr": "Böyle bir sistem türü bulunmuyor.",
    "fr": "Système introuvable.",
    "es": "Sistema no existe.",
    "de": "System nicht vorhanden.",
})

FAIL_NOTITLE = _({
    "en": "Title must be given.",
    "tr": "Başlık belirtilmeli.",
    "fr": "Vous devez donner un titre.",
    "es": "Favor ingresar un título.",
    "de": "Bitte einen Titel eingeben.",
})

FAIL_NOROOT = _({
    "en": "Root drive must be given.",
    "tr": "Kök sürücü belirtilmeli.",
    "fr": "Vous devez indiquer une partition racine.",
    "es": "Partición raíz debe ser indicada.",
    "de": "Root-Partition muss angegeben werden.",
})

FAIL_NOKERNEL = _({
    "en": "Kernel path must be given.",
    "tr": "Çekirdek yolu belirtilmeli.",
    "fr": "Vous devez indiquer le chemin vers le noyau.",
    "es": "Ruta al kernel debe ser ingresado.",
    "de": "Bitte Pfad zum Kernel eingeben.",
})

FAIL_KERNEL_IN_USE = _({
    "en": "Kernel is in use or not installed: '%s'",
    "tr": "Çekirdek kullanımda ya da yüklü değil: '%s'",
    "fr": "Soit le noyau est en cours d'utilisation, soit il n'est pas installé: %s",
    "es": "Kernel está en uso o no se encuentra: '%s'",
    "de": "Kernel ist gerade in Benutzung oder kann nicht gefunden werden: '%s'",
})

FAIL_KERNEL_VERSION = _({
    "en": "Kernel version must be in version-release(-suffix) format.",
    "tr": "Kernel sürümü sürüm-yayım(-uzantı) formatında olmalı.",
    "fr": "La version du noyau doit être mentionnée dans le format version-release(-suffixe)",
    "es": "Versión de kernel debe tener el formato version-release(-suffix).",
    "de": "Kernelversion muss im Format version-release(-suffix) sein.",
})

# Maximum old entries in alternate GRUB menu
MAX_ENTRIES = 2

# Configuration files
CONF_GRUB = "/boot/grub/grub.conf"
CONF_GRUB_ALT = "/boot/grub/grub-alt.conf"

# GRUB/Kernel directories
BOOT_DIR = "/boot"
GRUB_DIR = "/boot/grub"
MODULES_DIR = "/lib/modules"

# List of supported systems
# name: (Label, [required], [optional])
# required and optional values can be: root, kernel, initrd, options
CONF_SYSTEMS = {
    "linux": ("Linux", ["root", "kernel"], ["initrd", "options"]),
    "xen": ("Xen", ["root", "kernel"], ["initrd", "options"]),
    "windows": ("Windows", ["root"], []),
    "memtest": ("Memtest", ["root"], []),
}

# Required methods

def bootParameters(root):
    """
        Gets kernel boot parameters and strips unnecessary ones.

        Arguments:
            root: Root device
        Returns:
            Kernel options
    """

    s = []
    for i in [x for x in open("/proc/cmdline", "r").read().split() if not x.startswith("init=") and not x.startswith("xorg=")]:
        if i.startswith("root="):
            s.append("root=%s" % root)
        elif i.startswith("mudur="):
            mudur = "mudur="
            for p in i[len("mudur="):].split(','):
                if p == "livecd" or p == "livedisk": continue
                mudur += p
            if not len(mudur) == len("mudur="):
                s.append(mudur)
        else:
            s.append(i)
    return " ".join(s).strip()

def parseVersion(version):
    """
        Parses a kernel filename and returns kernel version and suffix. Raises ParseError

        Arguments:
            version: Kernel version, in version-release(-suffix) format. Suffix is optional.
        Returns:
            None on error, (version, suffix) on success.
    """

    try:
        k_version, x, x, k_suffix = re.findall("kernel-(([a-z0-9\._]+)-([0-9]+))(-.*)?", version)[0]
    except IndexError:
        return None
    return k_version, k_suffix

def groupEntries(grub, root):
    """
        Groups entries in GRUB configuration.

        Arguments:
            grub: GRUB configuration instance
            root: Root device
        Returns:
            Entries grouped by kernel and version
            e.g.:
            ({'pardus-pae': [4], 'other': [1, 3], 'pardus': [0, 2]}, {'pardus-pae': {4: '2.6.30.9-128'}, 'pardus': {0: '2.6.30.9-128', 2: '2.6.30.9-129'}})
    """

    groups = {}
    versions = {}

    def __addItem(_key, _index, _version=None):
        if _key not in groups:
            groups[_key] = []
        groups[_key].append(_index)
        if _version:
            if _key not in versions:
                versions[_key] = {}
            versions[_key][_index] = _version

    for i, title in enumerate(grub.listEntries()):
        # read entry
        entry = grub.getEntry(i)
        e_kernel = entry.getCommand("kernel")
        e_root = entry.getCommand("root")
        e_uuid = entry.getCommand("uuid")
        if e_kernel and "kernel-" in e_kernel.value and (e_root or e_uuid):
            # find linux device address
            rootDev = None
            if e_root:
                rootDev = linuxAddress(e_root.value)
            elif e_uuid:
                rootDev = getDeviceByUUID(e_uuid.value)
            # put all entries on other devices to a "other" list
            if rootDev != root:
                __addItem("other", i)
                continue
            # parse kernel version too see if it's Pardus kernel
            version = e_kernel.value.split("kernel-")[1].split(" ")[0]
            try:
                version, suffix = parseVersion("kernel-%s" % version)
            except (ValueError, TypeError):
                __addItem("other", i)
                continue
            if suffix:
                __addItem("pardus%s" % suffix, i, version)
            else:
                __addItem("pardus", i, version)
        else:
            # put all unknown entries to "other" list
            __addItem("other", i)

    return groups, versions

def addNewKernel(grub, version, root):
    """
        Adds new kernel entry to GRUB.

        Arguments:
            grub: GRUB configuration instance
            version: Kernel version, in version-release(-suffix) format. Suffix is optional.
            root: Root device
    """

    # get version and suffix
    version, suffix = parseVersion("kernel-%s" % version)

    groups, versions = groupEntries(grub, root)
    group_name = "pardus%s" % suffix

    default_index = grub.getOption("default", 0)
    if default_index != "saved":
        try:
            default_index = int(default_index)
        except ValueError:
            default_index = 0

    if group_name in versions and any([x == version for x in versions[group_name].values()]):
        # Version is already in list, do nothing
        entry_index = -1
        for i in versions[group_name]:
            if versions[group_name][i] == version:
                entry_index = i
                break
    else:
        if group_name in groups:
            entry_index = min(groups[group_name])
            # Get kernel options of first entry in group
            kernel = grub.getEntry(entry_index).getCommand("kernel")
            options = kernel.value.split(" ", 1)[1]
        else:
            entry_index = -1
            # Get kernel options from /proc/cmdline
            options = bootParameters(root)

        release = open("/etc/pardus-release", "r").readline().strip()
        title = "%s [%s%s]" % (release, version, suffix)

        entry = grubEntry(title)
        entry.setCommand("root", grubAddress(root))
        entry.setCommand("kernel", "/boot/kernel-%s%s %s" % (version, suffix, options))
        entry.setCommand("initrd", "/boot/initramfs-%s%s" % (version, suffix))
        if default_index == "saved":
            entry.setCommand("savedefault", "")
        grub.addEntry(entry, entry_index)

    # update default index, if it's after last entry
    if default_index != "saved":
        if default_index > entry_index and entry_index != -1:
            default_index += 1
            grub.setOption("default", default_index)

def moveOldKernels(grub, grub_alt, root):
    """
        Moves old kernels to other GRUB configuration file.

        Arguments:
            grub: GRUB configuration instance
            grub_alt: GRUB configuration instance for old entries
            root: Root device
    """

    groups, versions = groupEntries(grub, root)

    default_index = grub.getOption("default", 0)
    if default_index != "saved":
        try:
            default_index = int(default_index)
        except ValueError:
            default_index = 0

    entries = []
    for group_name in groups:
        if not group_name.startswith("pardus"):
            continue
        # get group entries
        group_entries = groups[group_name]
        # keep first entry of group
        group_entries.remove(min(group_entries))
        # add group entries to list of entries to be removed
        entries.extend(group_entries)

    # remove entries, start from the last one
    entries.sort(reverse=True)
    for entry_index in entries:
        entry = grub.getEntry(entry_index)
        grub.removeEntry(entry)
        grub_alt.addEntry(entry, 0)

        if default_index != "saved":
            # update default index, if it's before removed entry
            if default_index > entry_index:
                default_index -= 1
                grub.setOption("default", default_index)

def regroupKernels(grub, root, max_entries=3):
    """
        Regroups kernels in GRUB configuration file and remove unnecessary kernels.
        This method is used to shorten GRUB configuration file for old kernels.

        Arguments:
            grub: GRUB configuration instance
            root: Root device
            max_entries: Number of entries in each group
    """

    groups, versions = groupEntries(grub, root)

    entries = []
    for group_name in groups:
        if not group_name.startswith("pardus"):
            continue
        # get group entries
        group_entries = groups[group_name]
        group_entries.sort()
        # add group entries to list of entries to be removed
        # keep `max_entries` entries
        entries.extend(group_entries[max_entries:])

    # remove entries, start from the last one
    entries.sort(reverse=True)
    for entry_index in entries:
        entry = grub.getEntry(entry_index)
        grub.removeEntry(entry)

def copyOptions(grub, grub_alt):
    """
        Exports GRUB options to other configuration file.

        Arguments:
            grub: GRUB configuration instance
            grub_alt: GRUB configuration instance for old entries
    """

    for key in grub.listOptions():
        if key not in ["timeout"]:
            grub_alt.setOption(key, grub.getOption(key))

def addLinks(grub, grub_alt, grub_fn, grub_fn_alt):
    """
        Adds menu links between two GRUB configuration files.

        Arguments:
            grub: GRUB configuration instance
            grub_alt: GRUB configuration instance for old entries
            grub_fn: File name of main GRUB configuration
            grub_fn_alt: File name of alternative GRUB configuration
    """

    def _removeLink(_grub, _file):
        """
            Removes a link from specified GRUB configuration.
            Doesn't break default boot index.

            Arguments:
                _grub: GRUB configuration instance
                _file: Target file
        """
        # Get default index
        default_index = grub.getOption("default", 0)
        if default_index != "saved":
            try:
                default_index = int(default_index)
            except ValueError:
                default_index = 0
        # Find and remove link entry
        for index, entry in enumerate(_grub.entries):
            if entry.getCommand("configfile") and entry.getCommand("configfile").value == _file:
                _grub.removeEntry(entry)
                if default_index != "saved":
                    # Fix default index, if necessary
                    if index < default_index:
                        default_index -= 1
                        grub.setOption("default", default_index)

    def _addLink(_grub, _file, _title):
        """
            Adds a link to specified GRUB configuration.

            Arguments:
                _grub: GRUB configuration instance
                _file: Target file
                _title: Entry title
        """
        if not any([x.getCommand("configfile") and x.getCommand("configfile").value == _file for x in _grub.entries]):
            entry = grubEntry(_title)
            entry.setCommand("configfile", _file)
            _grub.addEntry(entry)

    # Remove link to ALTERNATIVE file in main GRUB configuration
    _removeLink(grub, grub_fn_alt)
    # Remove link to MAIN file in alternative GRUB configuration
    _removeLink(grub_alt, grub_fn)

    if len(grub_alt.entries) > 0:
        # Add link to ALTERNATIVE file in main GRUB configuration
        _addLink(grub, grub_fn_alt, MSG_OLD_KERNELS)
        # Add link to MAIN file in alternative GRUB configuration
        _addLink(grub_alt, grub_fn, MSG_MAIN_MENU)

# FIXME: Refactor
def parseGrubEntry(entry):
    os_entry = {
        "os_type": "unknown",
        "title": entry.title,
    }
    for command in entry.commands:
        key = command.key
        value = command.value

        if key in ["root", "rootnoverify"]:
            os_entry["root"] = linuxAddress(value)

        elif key == "uuid":
            os_entry["uuid"] = value

        elif key == "initrd":
            os_entry["initrd"] = value
            if os_entry["initrd"].startswith("("):
                os_entry["initrd"] = os_entry["initrd"].split(")", 1)[1]

        elif key == "kernel":
            try:
                kernel, options = value.split(" ", 1)
                os_entry["kernel"] = kernel
                os_entry["options"] = options
            except ValueError:
                os_entry["kernel"] = value
            os_entry["os_type"] = "linux"
            if os_entry["kernel"].startswith("("):
                root, kernel = os_entry["kernel"].split(")", 1)
                os_entry["root"] = linuxAddress(root + ")")
                os_entry["kernel"] = kernel
            if os_entry["kernel"] == "/boot/xen.gz":
                os_entry["os_type"] = "xen"
            elif os_entry["kernel"] == "/boot/memtest":
                os_entry["os_type"] = "memtest"
                del os_entry["kernel"]

        elif key in ["chainloader", "makeactive"]:
            os_entry["os_type"] = "windows"

        elif key == "savedefault":
            os_entry["default"] = "saved"

        elif key == "module" and os_entry["os_type"] == "xen":
            if value.startswith("("):
                value = value.split(")", 1)[1]
            if value.startswith("/boot/kernel"):
                if " " in value:
                    os_entry["kernel"], os_entry["options"] = value.split(" ", 1)
                else:
                    os_entry["kernel"] = value
            elif value.startswith("/boot/init"):
                os_entry["initrd"] = value
    return os_entry

def makeGrubEntry(title, os_type, root=None, kernel=None, initrd=None, options=None):
    if os_type not in CONF_SYSTEMS:
        fail(FAIL_NOSYSTEM)

    fields_req = CONF_SYSTEMS[os_type][1]
    fields_opt = CONF_SYSTEMS[os_type][2]
    fields_all = fields_req + fields_opt

    if "root" in fields_all:
        if "root" in fields_req and not root:
            fail(FAIL_NOROOT)

        uuid = None
        if not root.startswith("/dev/") and os_type not in ["windows", "memtest"]:
            uuid = root
        else:
            try:
                linux_disk, linux_part, grub_disk, grub_part = parseLinuxDevice(root)
            except (ValueError, TypeError):
                fail(FAIL_NODEVICE % root)
            grub_device = "(%s,%s)" % (grub_disk, grub_part)

    if "kernel" in fields_req and not kernel:
        fail(FAIL_NOKERNEL)

    entry = grubEntry(title)

    if os_type == "windows":
        # If Windows is not on first disk...
        if grub_disk != "hd0":
            entry.setCommand("map", "(%s) (hd0)" % grub_disk)
            entry.setCommand("map", "(hd0) (%s)" % grub_disk, append=True)
        entry.setCommand("rootnoverify", grub_device)
        entry.setCommand("makeactive", "")
        entry.setCommand("chainloader", "+1")
    else:
        if uuid:
            entry.setCommand("uuid", uuid)
        elif root:
            entry.setCommand("root", grub_device)
    if os_type == "xen":
        entry.setCommand("kernel", "/boot/xen.gz")
        if kernel and "kernel" in fields_all:
            if options and "options" in fields_all:
                entry.setCommand("module", "%s %s" % (kernel, options))
            else:
                entry.setCommand("module", kernel)
        if initrd and "initrd" in fields_all:
            entry.setCommand("module", initrd, append=True)
    elif os_type == "memtest":
        if uuid:
            entry.setCommand("uuid", uuid)
        elif root:
            entry.setCommand("root", grub_device)
        entry.setCommand("kernel", "/boot/memtest")
    else: # linux
        if kernel and "kernel" in fields_all:
            if options and "options" in fields_all:
                entry.setCommand("kernel", "%s %s" % (kernel, options))
            else:
                entry.setCommand("kernel", kernel)
        if initrd and "initrd" in fields_all:
            entry.setCommand("initrd", initrd)
    return entry

def removeKernel(version):
    """
        Removes specified kernel and it's modules from system.

        Arguments:
            version: Kernel version
    """

    dir_modules = os.path.join(MODULES_DIR, version)
    if os.path.exists(dir_modules):
        shutil.rmtree(dir_modules)

    files_kernel = ["kernel", "System.map", "Module.sysmvers", "initramfs", "initrd", "vmlinux"]
    for _file in files_kernel:
        _file = os.path.join(BOOT_DIR, "%s-%s" % (_file, version))
        if os.path.exists(_file):
            os.unlink(_file)

# Boot.Loader methods

def updateKernelEntry(version, root):
    # Root device
    if not len(root):
        root = getRoot()

    # Kernel version
    if not len(version):
        version = os.uname()[2]

    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    # Alternative menu configuration
    grub_alt = grubConf()
    if os.path.exists(CONF_GRUB_ALT):
        grub_alt.parseConf(CONF_GRUB_ALT)

    # Copy options to alternative configuration.
    copyOptions(grub, grub_alt)

    # Add new kernel to main configuration.
    addNewKernel(grub, version, root)

    # Move old kernels to alternative configuration.
    moveOldKernels(grub, grub_alt, root)

    # Regroup kernels in alternative configuration. This will shorten list.
    regroupKernels(grub_alt, root, MAX_ENTRIES)

    # Add cross links between two configuration files.
    addLinks(grub, grub_alt, CONF_GRUB, CONF_GRUB_ALT)

    # Save changes to both files.
    grub.write(CONF_GRUB)
    grub_alt.write(CONF_GRUB_ALT)

    # Notify all COMAR clients
    notify("Boot.Loader", "Changed", "option")

def listSystems():
    return CONF_SYSTEMS

def getOptions():
    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    # Default options
    options = {
        "default": grub.getOption("default", "0"),
        "timeout": grub.getOption("timeout", "0"),
    }

    # Password
    if "password" in grub.options:
        options["password"] = "yes"

    # Background color
    if "background" in grub.options:
        options["background"] = grub.getOption("background")

    # Get splash image, strip device address
    if "splashimage" in grub.options:
        splash = grub.getOption("splashimage")
        if ")" in splash:
            splash = splash.split(")")[1]
        options["splash"] = splash

    return options

def setOption(option, value):
    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    # Alternate menu configuration
    grub_alt = grubConf()
    if os.path.exists(CONF_GRUB_ALT):
        grub_alt.parseConf(CONF_GRUB_ALT)

    if option == 'default':
        grub.setOption("default", value)
        for index, entry in enumerate(grub.entries):
            if value == "saved":
                entry.setCommand("savedefault", "")
            else:
                entry.unsetCommand("savedefault")
        default_entry = os.path.join(GRUB_DIR, "default")
        if not os.path.exists(default_entry):
            file(default_entry, "w").write("\x00\x30\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a")
    elif option in 'timeout':
        grub.setOption("timeout", value)
    elif option == 'password':
        #grub.setOption("password", "--md5 %s" % md5crypt(value))
        grub.setOption("password", value)
    elif option == 'background':
        grub.setOption("background", value)
    elif option == 'splash':
        root = getRoot()
        root_grub = grubAddress(root)
        grub.setOption("splashimage", "%s%s" % (root_grub, value))

    # Copy options to alternative configuration.
    copyOptions(grub, grub_alt)

    # Save changes to both files.
    grub.write(CONF_GRUB)
    grub_alt.write(CONF_GRUB_ALT)

    # Notify all COMAR clients
    notify("Boot.Loader", "Changed", "option")

def listEntries():
    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    entries = []
    for index, entry in enumerate(grub.entries):
        os_entry = parseGrubEntry(entry)
        if os_entry["os_type"] == "unknown":
            continue
        os_entry["index"] = str(index)
        if not entry.getCommand("savedefault"):
            default_index = grub.getOption("default", "0")
            if default_index != "saved" and int(default_index) == index:
                os_entry["default"] = "yes"
        entries.append(os_entry)

    return entries

def removeEntry(index, title, uninstall):
    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    index = int(index)

    # Check entry title
    entry = grub.entries[index]
    if entry.title != title:
        fail(FAIL_NOENTRY)

    # Get default index
    default_index = grub.getOption("default", 0)
    if default_index != "saved":
        try:
            default_index = int(default_index)
        except ValueError:
            default_index = 0

    # Remove entry
    grub.removeEntry(entry)

    # Fix default index, if necessary
    if default_index != "saved":
        if index < default_index:
            default_index -= 1
            grub.setOption("default", default_index)

    # Save changes to both files.
    grub.write(CONF_GRUB)

    # Notify all COMAR clients
    notify("Boot.Loader", "Changed", "entry")

    if uninstall == "yes":
        os_entry = parseGrubEntry(entry)
        if os_entry["os_type"] in ["linux", "xen"] and os_entry["root"] == getRoot():
            kernel_version = os_entry["kernel"].split("kernel-")[1]
            removeKernel(kernel_version)

def setEntry(title, os_type, root, kernel, initrd, options, default, index):
    if not len(title):
        fail(FAIL_NOTITLE)

    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    # Alternative menu configuration
    grub_alt = grubConf()
    if os.path.exists(CONF_GRUB_ALT):
        grub_alt.parseConf(CONF_GRUB_ALT)

    index = int(index)

    entry = makeGrubEntry(title, os_type, root, kernel, initrd, options)

    if index == -1:
        grub.addEntry(entry)
    else:
        grub.entries[index] = entry

    if default == "yes":
        grub.setOption("default", index)
    elif default == "saved":
        grub.setOption("default", "saved")
        for index, entry in enumerate(grub.entries):
            entry.setCommand("savedefault", "")
    elif default == "no" and index != -1:
        default_index = grub.getOption("default", "0")
        if default_index != "saved" and int(default_index) == index:
            grub.setOption("default", "0")

    # Relocate links
    addLinks(grub, grub_alt, CONF_GRUB, CONF_GRUB_ALT)

    # Save changes to both files.
    grub.write(CONF_GRUB)

    # Notify all COMAR clients
    notify("Boot.Loader", "Changed", "option")

def listUnused():
    # Main menu configuration
    grub = grubConf()
    if os.path.exists(CONF_GRUB):
        grub.parseConf(CONF_GRUB)

    root = getRoot()

    # Find kernel entries
    kernels_in_use = []
    for entry in grub.entries:
        os_entry = parseGrubEntry(entry)

        # os_entry can have root or uuid depending on the distribution
        if os_entry["os_type"] in ["linux", "xen"]:
            if os_entry.get("root", "") == root or getDeviceByUUID(os_entry.get("uuid", "")) == root:
                kernel_version = os_entry["kernel"].split("kernel-")[1]
                kernels_in_use.append(kernel_version)

    # Find installed kernels
    kernels_installed = []
    for _file in os.listdir(BOOT_DIR):
        if _file.startswith("kernel-"):
            kernel_version = _file.split("kernel-")[1]
            kernels_installed.append(kernel_version)

    kernels_unused = set(kernels_installed) - set(kernels_in_use)
    kernels_unused = list(kernels_unused)

    return kernels_unused

def removeUnused(version):
    if not version or version not in listUnused():
        fail(FAIL_KERNEL_IN_USE % version)
    removeKernel(version)
