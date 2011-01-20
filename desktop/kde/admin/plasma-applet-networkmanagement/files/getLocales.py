#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

locales = ("de", "es", "fr", "hu", "it", "nl", "ru", "sv", "tr")
files = ("libknetworkmanager.po", "plasma_applet_networkmanagement.po")
podirname = "po"

cmaketemplate="""find_package(Gettext REQUIRED)
file(GLOB _po_files *.po)
GETTEXT_PROCESS_PO_FILES(tr ALL INSTALL_DESTINATION ${LOCALE_INSTALL_DIR} ${_po_files} )                                                                                                                                                      """

try:
    shutil.rmtree(podirname)
except:
    pass

os.mkdir(podirname)

for lang in locales:
    os.system("svn export svn://anonsvn.kde.org/home/kde/trunk/l10n-kde4/%s/messages/extragear-base/ %s/%s" % (lang, podirname, lang))
    for f in os.listdir("%s/%s" % (podirname, lang)):
        if not f in files:
            os.remove("%s/%s/%s" % (podirname, lang, f))

    cmake = open("%s/%s/CMakeLists.txt" % (podirname, lang), "w")
    cmake.write(cmaketemplate)
    cmake.close()
