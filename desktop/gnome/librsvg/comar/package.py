#!/usr/bin/python
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules")
    os.system("/usr/bin/gdk-pixbuf-query-loaders > /etc/gtk-2.0/gdk-pixbuf.loaders")

def preRemove():
    pass
