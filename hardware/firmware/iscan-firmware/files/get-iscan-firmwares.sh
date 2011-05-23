#!/bin/bash

FWS="Epson_Stylus_CX4400 GT-1500 GT-F670 GT-F700 GT-F720 GT-S80 GT-S600 GT-X750 GT-X770 GT-X820 Perfection_V30 Perfection_V330 iscan-network-nt"
URL="http://linux.avasys.jp/drivers/iscan-plugins/"

if [ ! -d iscan-firmware ]; then
    wget -nd -np -r -e robots=off -P iscan-firmware --accept=i386.rpm,x86_64.rpm $URL
fi

cd iscan-firmware
for fwrpm in $(ls *.rpm 2>/dev/null); do
    rpm2targz $fwrpm
    rm -f $fwrpm
done

for fwtargz in $(ls *.tar.gz); do
    tar xvf $fwtargz
done

