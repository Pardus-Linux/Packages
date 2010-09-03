import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/texmf-update")

def preRemove():
    os.system("/usr/sbin/texmf-update")
