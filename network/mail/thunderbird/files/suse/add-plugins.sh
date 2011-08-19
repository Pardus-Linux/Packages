#! /bin/sh
# Copyright (c) 2008 Wolfgang Rosenauer.  All rights reserved.
#

# check if we are started as root
# only one of UID and USER must be set correctly
if test "$UID" != 0 -a "$USER" != root; then
    echo "You must be root to start $0."
    exit 1
fi

PREFIX="/usr/lib/MozillaThunderbird"

# dictionaries
MYSPELL=/usr/share/hunspell
MOZ_SPELL=$PREFIX/dictionaries
if [ -d $MOZ_SPELL ] ; then
  if [ -d $MYSPELL ] ; then
    for dict in $MYSPELL/??[-_]??.aff ; do

      # check is it is really the file or it is a string which contain '??_??'
      if ! [ -e $dict ] ; then
        continue
      fi

      # the dict file name
      dict_file=`echo ${dict##*/}`

      # the dict file has a valid name
      lang=`echo ${dict_file:0:2}`
      country=`echo ${dict_file:3:2}`

      # check for .dic file
      if [ ! -r $MYSPELL/${lang}[-_]${country}.dic ] ; then
        continue
      fi

      # create links
      if [ ! -r $MOZ_SPELL/${lang}[-_]${country}.aff ] ; then
        ln -sf $MYSPELL/${lang}[-_]${country}.aff \
               $MOZ_SPELL/${lang}-${country}.aff
      fi      
      if [ ! -r $MOZ_SPELL/${lang}[-_]${country}.dic ] ; then
        ln -sf $MYSPELL/${lang}[-_]${country}.dic \
               $MOZ_SPELL/${lang}-${country}.dic
      fi      
    done
    echo "-> added hunspell dictionaries"
  fi

  # remove broken links
  for dict in $MOZ_SPELL/*.{aff,dic} ; do
    if ! [ -r $dict ] ; then
      rm -f $dict
    fi
  done
fi
