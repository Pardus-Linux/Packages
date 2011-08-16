#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import *

lo_base_path = "/opt/LibreOffice/lib/libreoffice/"
lo_program_path = lo_base_path + "program/"
programName = os.path.basename(sys.argv[0])
params = sys.argv[1:]

# Since we disable kde4 interface LO fallbacks to LO style open/save dialogs
# We force LO to gnome interface to use Gnome open/save dialogs.
os.environ['OOO_FORCE_DESKTOP'] = "gnome"

if os.path.isfile(os.path.join(lo_program_path, programName)):
    program = os.path.join(lo_program_path, programName)

# This transforms lowriter into swriter, lobase into sbase etc.
elif os.path.isfile(os.path.join(lo_program_path, "s" + programName[2:])):
    program = os.path.join(lo_program_path, "s" + programName[2:])

elif programName == "loweb":
    program = os.path.join(lo_program_path, "soffice")
    params.insert(0, "--web")

elif programName == "libreoffice":
    program = os.path.join(lo_program_path, "soffice")

else:
    raise Exception("Not a recognized program name!")

args = [program]
args.extend(params)
process = Popen(args)
process.wait()
sys.exit(process.returncode)
