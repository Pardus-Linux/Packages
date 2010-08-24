
if [ "$SESSION" = "kde" -o "$SESSION" = "kde-safe" -o "$SESSION" = "openbox-kde" ]; then
    kdehome=$HOME/.kde4
    test -n "$KDEHOME" && kdehome=`echo "$KDEHOME"|sed "s,^~/,$HOME/,"`

    # see kstartupconfig source for usage
    mkdir -m 700 -p $kdehome/share
    mkdir -m 700 -p $kdehome/share/config
    cat >$kdehome/share/config/startupconfigkeys <<EOF
kcminputrc Mouse cursorTheme 'Oxygen_Black'
kcminputrc Mouse cursorSize ''
ksplashrc KSplash Theme Default
ksplashrc KSplash Engine KSplashX
kcmrandrrc Display ApplyOnStartup false
kcmrandrrc [Screen0]
kcmrandrrc [Screen1]
kcmrandrrc [Screen2]
kcmrandrrc [Screen3]
kcmfonts General forceFontDPI 0
kdeglobals Locale Language '' # trigger requesting languages from KLocale
EOF
    kstartupconfig4
    returncode=$?
    if test $returncode -ne 0; then
        xmessage -geometry 500x100 "kstartupconfig4 does not exist or fails. The error code is $returncode. Check your installation."
        exit 1
    fi
    [ -r $kdehome/share/config/startupconfig ] && . $kdehome/share/config/startupconfig

    # XCursor mouse theme needs to be applied here to work even for kded or ksmserver
    if test -n "$kcminputrc_mouse_cursortheme" -o -n "$kcminputrc_mouse_cursorsize" ; then
        XCURSOR_PATH=/usr/kde/4/share/icons:$XCURSOR_PATH":~/.icons:/usr/share/icons:/usr/share/pixmaps:/usr/X11R6/lib/X11/icons"; export XCURSOR_PATH

        kapplymousetheme "$kcminputrc_mouse_cursortheme" "$kcminputrc_mouse_cursorsize"
        if test $? -eq 10; then
            XCURSOR_THEME=default
            export XCURSOR_THEME
        elif test -n "$kcminputrc_mouse_cursortheme"; then
            XCURSOR_THEME="$kcminputrc_mouse_cursortheme"
            export XCURSOR_THEME
        fi
        if test -n "$kcminputrc_mouse_cursorsize"; then
            XCURSOR_SIZE="$kcminputrc_mouse_cursorsize"
            export XCURSOR_SIZE
        fi
    fi

    if test -z "$XDG_DATA_DIRS"; then
        XDG_DATA_DIRS="`kde4-config --prefix`/share:/usr/share:/usr/local/share"
        export XDG_DATA_DIRS
    fi

    KDE_FULL_SESSION=true
    export KDE_FULL_SESSION

    KDE_SESSION_VERSION=4
    export KDE_SESSION_VERSION

    KDE_SESSION_UID=`id -ru`
    export KDE_SESSION_UID
fi
