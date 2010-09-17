#!/usr/bin/python

import os
import grp
import pwd
import shutil

### Helper methods

def hav(method, args):
    try:
        call("baselayout", "User.Manager", method, args)
    except:
        pass

def deleteGroup(group):
    try:
        gid = grp.getgrnam(group)[2]
        # deleteGroup(gid)
        hav("deleteGroup", (gid))
    except KeyError:
        pass

def deleteUser(user):
    try:
        uid = pwd.getpwnam(user)[2]
        # deleteUser(uid, delete_files)
        hav("deleteUser", (uid, False))
    except KeyError:
        pass

def migrateUsers():
    # build user -> group map for migration (hopefully we'll drop this in 2012)
    migration = []
    migrationMap = {
                    "cdrom"     : "removable",
                    "plugdev"   : "removable",
                    "lp"        : "pnp",
                    "scanner"   : "pnp",
                   }
    for user in pwd.getpwall():
        groups = set()
        if 1000 <= user.pw_uid < 65534:
            for group in grp.getgrall():
                if user.pw_name in group.gr_mem:
                    groups.add(group.gr_name)

            for oldGroup, newGroup in migrationMap.items():
                if oldGroup in groups:
                    groups.remove(oldGroup)
                    groups.add(newGroup)

            if groups:
                migration.append((user.pw_uid, list(groups)))

    # Migrate regular user groups
    for user, group in migration:
        # setUser(uid, realname, homedir, shell, passwd, groups)
        hav("setUser", (user, "", "", "", "", group))


### COMAR methods

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # We don't want to overwrite an existing file during upgrade
    specialFiles = ["passwd", "shadow", "group", "fstab", "hosts", "ld.so.conf", "resolv.conf"]

    for specialFile in specialFiles:
        if not os.path.exists("/etc/%s" % specialFile):
            shutil.copy("/usr/share/baselayout/%s" % specialFile, "/etc")

    shutil.copy("/etc/passwd", "/usr/share/baselayout/passwd.backup")
    shutil.copy("/etc/group", "/usr/share/baselayout/group.backup")

    if fromRelease and int(fromRelease) < 143:
        # Release 143 starts using /etc/ld.so.conf.d. Copy ld.so.conf
        # for "include" statement.
        shutil.copy("/usr/share/baselayout/ld.so.conf", "/etc")

    # First delete/add polkit group/user, because we use polkit-python in addgroup/delete methods of COMAR
    deleteGroup("polkit")
    hav("addGroup", (103, "polkit"))

    deleteUser("polkit")
    hav("addUser", (103, "polkit", "PolicyKit", "/dev/null", "/bin/false", "", ["polkit"], [], []))

    ##################################
    # Merge new system groups
    # addGroup(gid, name)
    groups = (
                (30,  "squid"),
                (50,  "named"),
                # For systemd/var-lock.mount
                (54,  "lock"),
                (60,  "mysql"),
                (70,  "postgres"),
                (80,  "apache"),
                (90,  "dovecot"),
                (100, "users"),
                (102, "hal"),
                (104, "postfix"),
                (105, "postdrop"),
                (106, "smmsp"),
                (107, "locate"),
                (108, "utmp"),
                (109, "firebird"),
                (110, "dhcp"),
                (111, "ldap"),
                (112, "clamav"),
                (113, "ntlmaps"),
                (120, "avahi"),
                (121, "avahi-autoipd"),
                (123, "ntp"),
                (130, "tss"),
                (131, "ejabberd"),
                (132, "tomcat"),
                (133, "ups"),
                (134, "partimag"),
                (135, "radiusd"),
                (136, "oprofile"),
                (137, "mediatomb"),
                # 'pulse' is for system wide PA daemon.
                (138, "pulse"),
                # In order to access to a system wide PA daemon,
                # a user should be a member of the 'pulse-access' group.
                (139, "pulse-access"),
                (141, "italc"),
                (142, "quassel"),
                (143, "bitlbee"),
                (144, "icecast"),
                (145, "virt"),
                # Gnokii system user for the SMS daemon
                (146, "gnokii"),
                (150, "svn"),
                (151, "memcached"),
                (152, "rtkit"),
                # NetworkManager user for OpenConnect VPN helper
                (153, "nm-openconnect"),
                (154, "qemu"),
                (155, "kvm"),
                (160, "usbmuxd"),
                (161, "openvpn"),
                (162, "privoxy"),
                (163, "kvm"),
                (164, "qemu"),
                (165, "kdm"),
                # COMAR profile groups
                (200, "pnp"),
                (201, "removable"),
                (202, "netuser"),
                (203, "netadmin"),
                (204, "power"),
                (205, "pnpadmin"),
                # for RT jackaudio
                (206, "jackuser"),
            )

    for gid, groupName in groups:
        try:
            grp.getgrnam(groupName)
        except KeyError:
            hav("addGroup", (gid, groupName))
        else:
            # Group already exists, remove and add back
            # FIXME: Implement setGroup in usermgr.py for this
            deleteGroup(groupName)
            hav("addGroup", (gid, groupName))


    ##################################
    # Merge new system users
    # addUser(uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths)

    users = (
                (20,  "dialout", "Dialout", "/dev/null", "/bin/false", "", ["dialout"], [], []),
                (30,  "squid", "Squid", "/var/cache/squid", "/bin/false", "", ["squid"], [], []),
                (40,  "named", "Bind", "/var/bind", "/bin/false", "", ["named"], [], []),
                (60,  "mysql", "MySQL", "/var/lib/mysql", "/bin/false", "", ["mysql"], [], []),
                (70,  "postgres", "PostgreSQL", "/var/lib/postgresql", "/bin/false", "", ["postgres"], [], []),
                (80,  "apache", "Apache", "/dev/null", "/bin/false", "", ["apache", "svn"], [], []),
                (90,  "dovecot", "Dovecot", "/dev/null", "/bin/false", "", ["dovecot"], [], []),
                (102, "hal", "HAL", "/dev/null", "/bin/false", "", ["hal"], [], []),
                (104, "postfix", "Postfix", "/var/spool/postfix", "/bin/false", "", ["postfix"], [], []),
                (106, "smmsp", "smmsp", "/var/spool/mqueue", "/bin/false", "", ["smmsp"], [], []),
                (109, "firebird", "Firebird", "/opt/firebird", "/bin/false", "", ["firebird"], [], []),
                (110, "dhcp", "DHCP", "/dev/null", "/bin/false", "", ["dhcp"], [], []),
                (111, "ldap", "OpenLDAP", "/dev/null", "/bin/false", "", ["ldap"], [], []),
                (112, "clamav", "Clamav", "/dev/null", "/bin/false", "", ["clamav"], [], []),
                (113, "ntlmaps", "NTLMaps", "/dev/null", "/bin/false", "", ["ntlmaps"], [], []),
                (120, "avahi", "Avahi mDNS/DNS-SD Stack", "/var/run/avahi-daemon", "/sbin/nologin", "", ["avahi"], [], []),
                (121, "avahi-autoipd", "Avahi IPv4LL Stack", "/var/lib/avahi-autoipd", "/sbin/nologin", "", ["avahi-autoipd"], [], []),
                (123, "ntp", "NTP", "/dev/null", "/bin/false", "", ["ntp"], [], []),
                (130, "tss", "tss", "/var/lib/tpm", "/bin/false", "", ["tss"], [], []),
                (131, "ejabberd", "Ejabberd", "/var/lib/ejabberd", "/bin/false", "", ["ejabberd"], [], []),
                (132, "tomcat", "Tomcat", "/var/lib/tomcat", "/bin/false", "", ["tomcat"], [], []),
                (133, "ups", "UPS", "/var/lib/nut", "/bin/false", "", ["ups", "dialout", "tty", "pnp"], [], []),
                (134, "partimag", "Partimage", "/dev/null", "/bin/false", "", ["partimag"], [], []),
                (135, "radiusd", "Freeradius", "/dev/null", "/bin/false", "", ["radiusd"], [], []),
                (136, "oprofile", "oprofile", "/dev/null", "/bin/false", "", ["oprofile"], [], []),
                (137, "mediatomb", "mediatomb", "/dev/null", "/bin/false", "", ["mediatomb"], [], []),
                (138, "pulse", "PulseAudio System Daemon", "/var/run/pulse", "/bin/false", "", ["pulse", "pulse-access", "pulse-rt", "audio"], [], []),
                (139, "quasselcore", "Quassel IRC System", "/var/cache/quassel", "/bin/false", "", ["quassel"], [], []),
                (140, "bitlbee", "Bitlbee Gateway", "/var/lib/bitlbee", "/bin/false", "", ["bitlbee"], [], []),
                (141, "spamd", "Spamassassin Daemon", "/var/lib/spamd", "/bin/false", "", [], [], []),
                (145, "vboxadd", "VirtualBox Guest Additions", "/dev/null", "/bin/false", "", [], [], []),
                (146, "gnokii", "Gnokii system user", "/", "/sbin/nologin", "", ["gnokii"], [], []),
                (150, "svn", "Subversion", "/dev/null", "/bin/false", "", ["svn"], [], []),
                (151, "icecast", "Icecast Server", "/dev/null", "/bin/false", "", ["icecast"], [], []),
                (152, "memcached", "Memcached daemon", "/var/run/memcached", "/bin/false", "", ["memcached"], [], []),
                (153, "rtkit", "RealtimeKit", "/proc", "/sbin/nologin", "", ["rtkit"], [], []),
                (154, "nm-openconnect", "NetworkManager user for OpenConnect", "/", "/sbin/nologin", "", ["nm-openconnect"], [], []),
                (155, "qemu", "QEMU", "/", "/sbin/nologin", "", ["qemu", "kvm"], [], []),
                (160, "usbmuxd", "usbmuxd daemon", "/dev/null", "/bin/false", "", ["usbmuxd"], [], []),
                (161, "openvpn", "OpenVPN", "/etc/openvpn", "/sbin/nologin", "", ["openvpn"], [], []),
                (162, "privoxy", "Privoxy", "/etc/privoxy", "/sbin/nologin", "", ["privoxy"], [], []),
                (163, "qemu", "qemu user", "/", "/sbin/nologin", "", ["qemu", "kvm"], [], []),
                (165, "kdm", "kdm", "/var", "/sbin/nologin", "", ["kdm"], [], []),
                (200, "pnp", "PnP", "/dev/null", "/bin/false", "", ["pnp"], [], []),
                (250, "mpd", "Music Player Daemon", "/var/lib/mpd", "/bin/false", "", ["audio", "pulse", "pulse-access", "pulse-rt"], [], []),
            )

    for uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths in users:
        deleteUser(nick)
        hav("addUser", (uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths))

    # Migrate users to their new groups if any
    migrateUsers()

    # We should only install empty files if these files don't already exist.
    if not os.path.exists("/var/log/lastlog"):
        os.system("/bin/touch /var/log/lastlog")
    if not os.path.exists("/var/run/utmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /var/run/utmp")
    if not os.path.exists("/var/log/wtmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /var/log/wtmp")

    # Enable shadow groups
    os.system("/usr/sbin/grpconv")
    os.system("/usr/sbin/grpck -r &>/dev/null")

    # Create /root if not exists
    if not os.path.exists("/root/"):
        shutil.copytree("/etc/skel", "/root")
        os.chown("/root", 0, 0)
        os.chmod("/root", 0700)

    # Tell init to reload new inittab
    os.system("/sbin/telinit q")

    # Save user defined DNS
    if not os.access("/etc/resolv.default.conf", os.R_OK):
        os.system("cp /etc/resolv.conf /etc/resolv.default.conf")
