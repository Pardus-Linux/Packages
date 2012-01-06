#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # FIXME: All of these should be run only once during first install
    # but we can't do this in pisi, i think.

    # graphical.target is the default if xdm is enabled
    target = "/lib/systemd/system/graphical.target"

    # FIXME: We should clean this somewhere or else on every install of systemd
    # The default will get overriden by the old mudur service state
    # Maybe we can depend on the new mudur which will clean up around, or
    # mudur can be the one who creates this link
    if os.path.exists("/etc/mudur/services/disabled/xdm"):
        target = "/lib/systemd/system/multi-user.target"

    # set the default target if not set before
    if not os.path.islink("/etc/systemd/system/default.target"):
        os.symlink(target, "/etc/systemd/system/default.target")

    # Enable the services installed by default
    os.system("/bin/systemctl enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service")


# Fedora disables all services enabled in postInstall during preuninstall
# But do we really need this
#def preRemove():
#    os.system("/bin/systemctl disable \
#                getty@.service \
#                remote-fs.target \
#                systemd-readahead-replay.service \
#                systemd-readahead-collect.service")
#    try:
#       os.unlink("/etc/systemd/system/default.target")
#    except OSError:
#       pass
