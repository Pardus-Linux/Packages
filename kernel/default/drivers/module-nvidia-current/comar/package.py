#!/usr/bin/python

import os

base = "/usr/lib/nvidia-current"

oldPackages = ("nvidia_drivers177", "nvidia_drivers180", "xorg_video_nvidia180", "xorg_video_nvidia185")
currentPackage = "xorg_video_nvidia_current"

def enable(package):
    call(package.replace("-", "_"), "Xorg.Driver", "enable")

def migrate():
    configXML = "/var/lib/zorg/config.xml"
    if os.path.exists(configXML):
        import piksemel

        doc = piksemel.parse(configXML)
        dirty = False
        for card in doc.tags("Card"):
            ac = card.getTag("ActiveConfig")
            if ac:
                drv = ac.getTag("Driver")
                if drv:
                    pkg = drv.getAttribute("package")
                    if pkg:
                        pkg = pkg.replace("-", "_")
                        if drv.firstChild().data() == "nvidia" \
                            and (pkg in oldPackages):
                            drv.setAttribute("package", currentPackage)
                            drv.setData("nvidia-current")
                            dirty = True

        if dirty:
            open(configXML, "w").write(doc.toPrettyString())

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    migrate()

    try:
        enabledPackage = open("/var/lib/zorg/enabled_package").read().replace("-", "_")

        if enabledPackage in oldPackages \
            or (enabledPackage == currentPackage and fromVersion != toVersion):
            enable(currentPackage)

    except IOError:
        pass


    os.system("/usr/sbin/alternatives \
                --install /usr/lib/libGL.so.1.2 libGL %(base)s/libGL.so.1.2 50 \
                --slave /usr/lib/xorg/modules/volatile xorg-modules-volatile %(base)s/modules \
                --slave /etc/ld.so.conf.d/10-nvidia-current.conf nvidia-current-conf /usr/share/nvidia-current/ld.so.conf"
              % {"base" : base})

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2" % base)
    pass
