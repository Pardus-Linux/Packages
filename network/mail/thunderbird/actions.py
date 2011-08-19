#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir   = "thunderbird"
MOZAPPDIR = "/usr/lib/MozillaThunderbird"

locales = ["ca", "da", "de", "es-AR", "es-ES", "fr", "hu", "it", "nl", "pl", "pt-BR", "ru", "sv-SE", "tr"]

def setup():
    # Use autoconf 2.13, pff
    shelltools.chmod("autoconf-213/autoconf-2.13", 0755)

    # Set job count for make
    pisitools.dosed(".mozconfig", "%%JOBS%%", get.makeJOBS())

    # Set distro info
    pisitools.dosed(".pardus-default-prefs.js", "DISTRIB_ID", get.lsbINFO()["DISTRIB_ID"])
    pisitools.dosed(".pardus-default-prefs.js", "DISTRIB_RELEASE", get.lsbINFO()["DISTRIB_RELEASE"])

def build():
    # Build thunderbird
    autotools.make("-f client.mk build")

    # Prepare language packs
    for locale in locales:
        autotools.make("-C mail/locales langpack-%s" % locale)

    # Build enigmail
    #shelltools.cd("mailnews/extensions/enigmail")
    #shelltools.system("./makemake -r")
    #autotools.make("MOZ_CHROME_FILE_FORMAT=jar")
    #autotools.make("xpi")

def install_enigmail():
    # Install enigmail
    enigmail_dir = "extensions/{3550f703-e582-4d05-9a08-453d09bdfdc6}/{847b3a00-7ab1-11d4-8f02-006008948af5}"
    pisitools.dodir("%s/%s" % (MOZAPPDIR, enigmail_dir))

    shelltools.system("unzip %s/mozilla/dist/bin/enigmail-*.xpi -d %s/%s/%s" % (get.curDIR(), get.installDIR(), MOZAPPDIR, enigmail_dir))
    pisitools.remove("%s/enigmail-*.xpi" % MOZAPPDIR)

def install():
    pisitools.insinto("/usr/lib/", "mozilla/dist/bin", "MozillaThunderbird", sym=False)

    # Install language packs
    for locale in locales:
        pisitools.copytree("mozilla/dist/xpi-stage/locale-%s" % locale, "%s/usr/lib/MozillaThunderbird/extensions/langpack-%s@thunderbird.mozilla.org" % (get.installDIR(), locale))

    #install_enigmail()

    # Install default-prefs.js
    pisitools.insinto("%s/defaults/pref" % MOZAPPDIR, ".pardus-default-prefs.js", "all-pardus.js")

    # Empty fake files to get Turkish spell check support working
    pisitools.dodir("%s/extensions/langpack-tr@thunderbird.mozilla.org/dictionaries" % MOZAPPDIR)
    shelltools.touch("%s/%s/%s/dictionaries/tr-TR.aff" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))
    shelltools.touch("%s/%s/%s/dictionaries/tr-TR.dic" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))

    pisitools.removeDir("%s/dictionaries" % MOZAPPDIR)
    pisitools.dosym("/usr/share/hunspell", "%s/dictionaries" % MOZAPPDIR)

    # Remove useless file
    pisitools.remove("/usr/lib/MozillaThunderbird/.purgecaches")

    # Remove this to avoid spellchecking dictionary detection problems
    pisitools.remove("/usr/lib/MozillaThunderbird/defaults/pref/all-l10n.js")

    # Install icons
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")
    pisitools.insinto("%s/icons" % MOZAPPDIR, "other-licenses/branding/thunderbird/mailicon16.png")

    for s in (16, 22, 24, 32, 48, 256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "other-licenses/branding/thunderbird/mailicon%d.png" % s, "thunderbird.png")

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")
