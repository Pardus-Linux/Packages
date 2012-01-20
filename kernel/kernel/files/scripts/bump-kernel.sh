#!/bin/bash

# Usage: bump-kernel 2.6.32.9 will bump the kernel to 2.6.32.9

PATCH_URL="http://www.kernel.org/pub/linux/kernel/v2.6/patch-$1.bz2"
OLD_PATCH=`grep "<Patch.*>kernel/patch-.*</Patch>" pspec.xml | sed 's/.*<Patch.*>\(.*\)<\/Patch>/\1/'`

aria2c $PATCH_URL -d files/kernel

svn rm "files/$OLD_PATCH"
svn add "files/kernel/patch-$1.bz2"

sed -i "s:$OLD_PATCH:kernel/`basename $PATCH_URL`:" pspec.xml

# Change quilt series file
sed -i "s:^kernel/patch-2.6.*$:kernel/patch-$1 -p1:" files/series

bump $1 "$2"
