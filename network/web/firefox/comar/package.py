#!/usr/bin/python

import os

def symlink(src, dest):
    try:
        os.symlink(src, dest)
    except OSError:
        pass

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["HOME"] = "/root"
    os.system("/bin/touch /usr/lib/MozillaFirefox/components/compreg.dat")
    os.system("/bin/touch /usr/lib/MozillaFirefox/components/xpti.dat")
    os.system("/usr/lib/MozillaFirefox/firefox -register")
    os.system("/bin/touch /usr/lib/MozillaFirefox/.autoreg")

    if os.path.exists("/etc/mudur/language"):
        lang = open("/etc/mudur/language").read().strip()

        # Bookmarks & Search plugins
        if lang == "tr":
            symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-tr.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_tr.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
            symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_tr.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
        elif lang == "nl":
            symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-nl.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_nl.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
            symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_nl.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
        elif lang == "pt":
            symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_pt.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
            symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_pt.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
            #TODO: translate bookmarks to pt also.
            symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-en.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        elif lang == "de":
            symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-de.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_de.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
        else:
            symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-en.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_en.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
            symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_en.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")

def preRemove():
    try:
        os.unlink("/usr/lib/MozillaFirefox/.autoreg")
    except OSError:
        pass
