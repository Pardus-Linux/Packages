#!/bin/sh
#
# Customized agents startup file

if [ -x /usr/bin/gpg-agent ]; then
  eval "$(/usr/bin/gpg-agent --daemon)"
fi
