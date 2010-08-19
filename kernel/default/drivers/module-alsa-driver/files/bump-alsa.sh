#!/bin/bash

TODAY=`date +%Y%m%d`
SNAPSHOT="ftp://ftp.kernel.org/pub/linux/kernel/people/tiwai/snapshot/alsa-driver-$TODAY.tar.bz2"
FILENAME=`basename $SNAPSHOT`
URL="http://cekirdek.pardus.org.tr/~ozan/dist/sources/$FILENAME"

# Download and calculate sha1sum
wget $SNAPSHOT
SUM=`sha1sum $FILENAME | gawk '{ print $1 }'`

# Upload
scp $FILENAME ozan@cekirdek.pardus.org.tr:public_html/dist/sources

# Change the archive URL
sed -i "s,<Archive.*>.*</Archive>,<Archive sha1sum=\"$SUM\" type=\"tarbz2\">$URL</Archive>,g" pspec.xml

# Bump spec
bump "1.0.21_$TODAY" "Bump to the latest snapshot"

rm -rf $FILENAME

