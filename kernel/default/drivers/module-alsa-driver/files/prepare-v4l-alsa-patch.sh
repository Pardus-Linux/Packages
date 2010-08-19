#!/bin/bash

TEMPDIR=$(mktemp -d)
echo $TEMPDIR
CWD=$(pwd)

DRIVERS="saa7134 cx231xx cx88 em28xx"

cd $TEMPDIR
mkdir -p clean v4l

for d in $DRIVERS; do
    echo "Copying $d.."
    cp -r $1/drivers/media/video/$d v4l/
done

cd v4l

# Add toptree Makefile
cat << EOF > Makefile
#
# All media drivers should use the internal ALSA headers
#
NOSTDINC_FLAGS                  += -I\$(src)/../sound/include
NOSTDINC_FLAGS                  += -include config.h

#include \$(src)/../.config

EOF

for driver in $DRIVERS; do
    echo "obj-m += $driver/" >> Makefile
done

echo "Commenting external includes.."
grep -rl "^#include.*tuner-xc.*$" * | xargs sed -i "s/^\(#include.*tuner-xc.*$\)/\/*\1*\//g"

# Replace $CONFIG values with "m"
find -name "Makefile" | xargs sed -i 's/\$(CONFIG_VIDEO.*ALSA)/m/g'

# Drop modules other than the ALSA ones
find -name "Makefile" | xargs sed -i 's/^.*CONFIG_.*$//'

cd ..

# Create unified diff
echo "Creating patch.."
diff -Naur clean v4l > $CWD/add-v4l-alsa-drivers.patch

cd $CWD

rm -rf $TEMPDIR
