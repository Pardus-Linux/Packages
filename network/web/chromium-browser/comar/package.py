#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("xdg-icon-resource forceupdate --theme hicolor")

