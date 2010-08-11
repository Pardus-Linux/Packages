#!/bin/bash

NR=$(expr $(basename $(ls ~/2009/devel/kernel/default/kernel/files/kernel/0* | sort | tail -n1) | gawk -F'-' '{print $1}') + 1)
git format-patch --start-number=$NR $@

