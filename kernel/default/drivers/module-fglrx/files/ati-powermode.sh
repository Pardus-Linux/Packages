#!/bin/sh

#
# Control script for ACPI lid state and AC adapter state
#
# Copyright (c) 2006, ATI Technologies Inc.  All rights reserved.
#
# Fedora Modifications By Michael Larabel <Michael AT Phoronix.com> on July 5, 2006
# Pardus Modifications by Fatih Aşıcı <fatih at pardus.org.tr> on May 28, 2008

egrep -s ^ati-drivers$ /var/lib/zorg/enabled_package || exit 0

getXuser() {
        user=`who| grep -m1 ":$displaynum " | awk '{print $1}'`
        if [ x"$user" = x"" ]; then
                user=`who| grep -m1 ":$displaynum" | awk '{print $1}'`
        fi
        if [ x"$user" != x"" ]; then
                userhome=`getent passwd $user | cut -d: -f6`
                export XAUTHORITY=$userhome/.Xauthority
        else
                export XAUTHORITY=""
        fi
}


grep -q closed /proc/acpi/button/lid/*/state
if [ $? = 0 ]; then
 lid_closed=1
 echo "Lid Closed"
else
 lid_closed=0
 echo "Lid Open"
fi

grep -q off-line /proc/acpi/ac_adapter/*/state

if [ $? = 0 ]; then
   echo "On DC"
   on_dc=1
else
   echo "On AC"
   on_dc=0
fi



if [ ${lid_closed} -eq 1 -o ${on_dc} -eq 1 ]; then
    echo "Low power"
    for x in /tmp/.X11-unix/*; do
        displaynum=`echo $x | sed s#/tmp/.X11-unix/X##`
        getXuser;
        if [ x"$XAUTHORITY" != x"" ]; then
            export DISPLAY=":$displaynum"
            su $user -c "/usr/bin/aticonfig --set-powerstate=1 --effective=now"
        fi
    done
else
    echo "High power"
    for x in /tmp/.X11-unix/*; do
        displaynum=`echo $x | sed s#/tmp/.X11-unix/X##`
        getXuser;
        if [ x"$XAUTHORITY" != x"" ]; then
            export DISPLAY=":$displaynum"
            su $user -c "/usr/bin/aticonfig --set-powerstate=3 --effective=now"
        fi
    done
fi
