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

    # Bookmarks & Search plugins
    lang = open("/etc/env.d/03locale").readline().strip("LANG=")[:5]

    if lang == "tr_TR":
        symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-tr.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_tr.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_tr.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
    elif lang == "nl_NL":
        symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-nl.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_nl.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_nl.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
    elif lang == "pt_BR":
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_pt.xml", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.xml")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_pt.xml", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.xml")
        #TODO: translate bookmarks to pt also.
        symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-en.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
    elif lang == "de_DE":
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
