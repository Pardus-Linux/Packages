#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import comar
from comar.service import loadConfig

config_files = ("/etc/default/xdm",
                "/etc/conf.d/xdm")

xdm_path = "/usr/bin/xdm"
safe_xorg_conf = "/usr/share/X11/xorg-safe.conf"

if __name__ == "__main__":
    boot = "--boot" in sys.argv

    config = {}

    for config_file in config_files:
        cfg = loadConfig(config_file)
        config.update(cfg)

    dm_name = config.get("DISPLAY_MANAGER", "xdm")
    cursor_theme = config.get("XCURSOR_THEME")

    desktop_file = loadConfig("/usr/share/display-managers/%s.desktop" % dm_name)
    dm_path = desktop_file.get("Exec", xdm_path).split()[0]
    if cursor_theme is None:
        cursor_theme = desktop_file.get("X-Pardus-XCursorTheme")

    if not os.access(dm_path, os.X_OK):
        dm_path = xdm_path

    env = os.environ
    env["PATH"] = "/sbin:/usr/sbin:/bin:/usr/bin"

    try:
        locale = open("/etc/mudur/locale").read().rstrip()
        env["LC_ALL"] = locale
    except IOError:
        pass

    if cursor_theme:
        env["XCURSOR_THEME"] = cursor_theme

    link = comar.Link()
    # ready method will return False if sth is wrong or safe
    # mode is requested by user. But, what if we have no cards
    # and zorg returns False?
    if not link.Xorg.Display["zorg"].ready(boot, timeout=5*60):
        env["XORGCONFIG"] = safe_xorg_conf

    os.execl(dm_path, dm_path, "-nodaemon")
