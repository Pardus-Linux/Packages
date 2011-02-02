#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

#locales = ("de", "es", "fr", "hu", "it", "nl", "ru", "sv", "tr")
locales = ("de", "es", "fr", "hu", "it", "nl", "ru", "sv")
#files = ("libknetworkmanager.po", "plasma_applet_networkmanagement.po")
podirname = "po"
svnrepo = "svn+ssh://svn.kde.org/home/kde/branches/KDE/4.4/kde-l10n/%s/messages/kdepim/"

cmaketemplate="""find_package(Gettext REQUIRED)
file(GLOB _po_files *.po)
GETTEXT_PROCESS_PO_FILES(%s ALL INSTALL_DESTINATION ${LOCALE_INSTALL_DIR} ${_po_files} )"""

try:
    shutil.rmtree(podirname)
except:
    pass

os.mkdir(podirname)

maincmake = open("%s/CMakeLists.txt" % podirname, "w")

for lang in locales:
    os.system("svn export %s %s/%s" % (svnrepo % lang, podirname, lang))
    """
    for f in os.listdir("%s/%s" % (podirname, lang)):
        if not f in files:
            os.remove("%s/%s/%s" % (podirname, lang, f))
    """

    cmake = open("%s/%s/CMakeLists.txt" % (podirname, lang), "w")
    cmake.write(cmaketemplate % lang)
    cmake.close()

    maincmake.write("add_subdirectory(%s)\n" % lang)

maincmake.close()
