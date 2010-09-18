#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import glob
from subprocess import *

ooo_base_path = glob.glob("/opt/OpenOffice.org/lib/ooo-*/")[0]
ooo_program_path = ooo_base_path + "program/"
program=ooo_program_path+"s"+sys.argv[0].split('/')[-1][2:] # This transforms oowriter into swriter, oobase into sbase etc.
process=None

# Install zemberek if needed
install_zemberek = False

try:
    zemberek_version = open("/etc/zemberek-release").readlines()[0]

    try:
        local_zemberek_version = open(os.environ["HOME"]+"/.zemberek-release").readlines()[0]
        if float(zemberek_version) > float(local_zemberek_version):
            install_zemberek = True
    except IOError:
            install_zemberek = True
    except IndexError:
            install_zemberek = True

    if install_zemberek:
        os.system("%s/unopkg add -v -f /usr/share/zemberek/zemberek.zip" % ooo_program_path)

        fp = open(os.environ["HOME"]+"/.zemberek-release", "w")
        fp.write(zemberek_version)
        fp.close()

except IOError:
    print "Zemberek is missing!"

files = sys.argv[1:]
if files:
    for file in files:
        process = Popen(['kio-to-local',program,file])
else:
    process = Popen([program])

os.waitpid(process.pid,0)
