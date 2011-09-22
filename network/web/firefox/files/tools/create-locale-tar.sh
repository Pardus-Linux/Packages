#!/bin/bash

RELEASE_TAG="FIREFOX_6_0_2_RELEASE"
VERSION="6.0.2"

# These are Pardus supported languages. This list may changed by time to time
LOCALES="be ca de es-AR es-ES fr hu it nl pl ru sv-SE tr"

test ! -d l10n && mkdir l10n
for locale in $LOCALES
do
    hg clone http://hg.mozilla.org/releases/l10n/mozilla-release/$locale l10n/$locale
    [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
done

tar cjf l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

