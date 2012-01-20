#!/bin/bash

BRANCH=$1

if [ ! -d fedora-kernel ]; then
    fedora kernel
    git checkout origin/$1/master
fi

cd fedora-kernel

cat kernel.spec | egrep "^ApplyPatch.*\..*" > patches
vi patches # filter

for patch in `gawk '{print $2}' patches`; do
    echo $patch
done

rm -rf patches

