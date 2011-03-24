#!/bin/bash


BRANCH="releases/comm-1.9.2" # comm-central
RELEASE_TAG="THUNDERBIRD_3_1_9_RELEASE"
VERSION="3.1.9"

echo "cloning $BRANCH..."
hg clone http://hg.mozilla.org/$BRANCH thunderbird
pushd thunderbird
hg update -r $RELEASE_TAG
echo "running client.py..."
[ "$RELEASE_TAG" == "default" ] || _extra="--comm-rev=$RELEASE_TAG --mozilla-rev=$RELEASE_TAG"
# temporary!
_extra="--mozilla-repo=http://hg.mozilla.org/releases/mozilla-1.9.2 $_extra"
python client.py checkout --skip-chatzilla --skip-venkman $_extra
popd
echo "creating archive..."
tar cjf thunderbird-$VERSION-source.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS thunderbird

# l10n
# http://l10n.mozilla.org/dashboard/?tree=tb30x -> shipped-locales
echo "fetching locales..."
if [ -e shipped-locales ]; then
  SHIPPED_LOCALES=shipped-locales
else
  SHIPPED_LOCALES=thunderbird/mail/locales/shipped-locales
fi
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' $SHIPPED_LOCALES); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      echo "fetching $locale ..."
      hg clone http://hg.mozilla.org/releases/l10n-mozilla-1.9.2/$locale l10n/$locale
      hg -R l10n/$locale up -C -r $RELEASE_TAG
      ;;
  esac
done
echo "creating l10n archive..."
tar cjf l10n-$VERSION.tar.bz2 \
  --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=browser --exclude=calendar \
  --exclude=suite \
  l10n
