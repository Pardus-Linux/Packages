#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import *

lo_base_path = "/opt/LibreOffice/lib/libreoffice/"
lo_program_path = lo_base_path + "program/"
programName = os.path.basename(sys.argv[0])
params = sys.argv[1:]

if os.path.isfile(os.path.join(lo_program_path, programName)):
    program = os.path.join(lo_program_path, programName)

# This transforms lowriter into swriter, lobase into sbase etc.
elif os.path.isfile(os.path.join(lo_program_path, "s" + programName[2:])):
    program = os.path.join(lo_program_path, "s" + programName[2:])

elif programName == "loweb":
    program = os.path.join(lo_program_path, "swriter")
    params.insert(0, "--web")

else:
    raise Exception("Not a recognized program name!")

process = Popen([program].extend(params))
os.waitpid(process.pid,0)
