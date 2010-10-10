#!/bin/sh

. /etc/conf.d/virtualbox-guest

case $ACTION in
    add)
        if [ "x${LOAD_VBOXVFS_MODULE-true}" == "xtrue" ]; then
            /sbin/modprobe -s vboxvfs
        fi
        if [ -x /usr/sbin/VBoxService ]; then
            /usr/sbin/VBoxService $VBOXSERVICE_OPTS
        fi
        ;;

    remove)
        ;;

    *)
        exit 1
        ;;
esac
