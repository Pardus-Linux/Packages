#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # add disks into fstsb
    os.system("/sbin/update-fstab")

    # Convert Net.Link scripts to Network.Link
    fixNetworkProfiles()

def fixNetworkProfiles():
    import re

    PROFILE_DIR = "/etc/network"
    MAP = [
        ("namemode", "name_mode"),
        ("nameserver", "name_server"),
        ("authmode", "auth"),
        ("netmode", "net_mode"),
        ("mode", "net_mode"),
        ("address", "net_address"),
        ("mask", "net_mask"),
        ("gateway", "net_gateway"),
        ("user", "auth_username"),
        ("password", "auth_password"),
        ("user_anon", "auth_anon"),
        ("phase2", "auth_phase2"),
        ("ca_cert", "auth_cert_ca"),
        ("client_cert", "auth_cert_cli"),
        ("private_key", "auth_keyfile"),
        ("private_key_passwd", "auth_keyfile_passphrase"),
    ]

    for package in os.listdir(PROFILE_DIR):
        fn = os.path.join(PROFILE_DIR, package)
        if not os.path.isfile(fn):
            continue
        newlines = []
        for line in file(fn):
            line = line.strip()
            for old, new in MAP:
                line = re.sub("^%s" % old, new, line)
            newlines.append(line)
        newlines = "\n".join(newlines)

        file(fn, "w").write(newlines)
