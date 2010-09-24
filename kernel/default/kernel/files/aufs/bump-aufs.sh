#!/bin/bash

KVER=$1

git clone http://git.c3sl.ufpr.br/pub/scm/aufs/aufs2-standalone.git

cd aufs2-standalone
git checkout origin/aufs2.1-$KVER
cd ..

if [ -f aufs-2.1-$KVER.patch ]; then
    rm -f aufs-2.1-$KVER.patch
fi

for f in aufs2-standalone/fs/aufs/*; do
    diff -u /dev/null $f >> aufs-2.1-$KVER.patch
done

diff -u /dev/null aufs2-standalone/include/linux/aufs_type.h >> aufs-2.1-$KVER.patch

cp aufs2-standalone/{*base*,*kbuild*} .

rm -rf aufs2-standalone

svn add *.patch
