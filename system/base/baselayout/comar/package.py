#!/usr/bin/python

import os
import grp
import pwd
import shutil

def uniq(alist):
    s = {}
    return [s.setdefault(e,e) for e in alist if e not in s]

def hav(method, args):
    try:
        call("baselayout", "User.Manager", method, args)
    except:
        pass

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # We don't want to overwrite an existing file during upgrade
    specialFiles = ["hosts", "passwd", "shadow", "group", "fstab", "ld.so.conf", "resolv.conf"]

    for specialFile in specialFiles:
        if not os.path.exists("/etc/%s" % specialFile):
            shutil.copy("/usr/share/baselayout/%s" % specialFile, "/etc")

    shutil.copy("/etc/passwd", "/usr/share/baselayout/passwd.backup")
    shutil.copy("/etc/group", "/usr/share/baselayout/group.backup")

    # build user -> group map for migration
    migration = []
    for user in pwd.getpwall():
        groups = []
        if user[2] >= 1000 and user[2] < 65534:
            for group in grp.getgrall():
                if group[3].__contains__(user[0]):
                    groups.append(group[0])
            if groups.__contains__("cdrom"):
                groups.remove("cdrom")
                groups.append("removable")
            if groups.__contains__("plugdev"):
                groups.remove("plugdev")
                groups.append("removable")

            if groups.__contains__("lp"):
                groups.remove("lp")
                groups.append("pnp")
            if groups.__contains__("scanner"):
                groups.remove("scanner")
                groups.append("pnp")
            if len(groups) > 0:
                migration.append((user[2], uniq(groups)))

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

    #First delete/add polkit group/user, because we use polkit-python in addgroup/delete methods of COMAR
    deleteGroup("polkit")
    hav("addGroup", (103, "polkit"))
    deleteUser("polkit")
    hav("addUser", (103, "polkit", "PolicyKit", "/dev/null", "/bin/false", "", ["polkit"], [], []))

    # Remove old groups/users
    groups = ["apache",
              "avahi",
              "bitlbee",
              "clamav",
              "dhcp",
              "dovecot",
              "ejabberd",
              "firebird",
              "gnokii",
              "hal",
              "icecast",
              "italc",
              "kvm",
              "ldap",
              "locate",
              "mediatomb",
              "memcached",
              "mysql",
              "named",
              "netadmin",
              "netuser",
              "nm-openconnect",
              "ntlmaps",
              "ntp",
              "openvpn",
              "oprofile",
              "partimag",
              "pnp",
              "pnpadmin",
              "postdrop",
              "postfix",
              "postgres",
              "power",
              "pulse",
              "pulse-access",
              "pulse-rt",
              "qemu",
              "quassel",
              "radiusd",
              "removable",
              "rtkit",
              "smmsp",
              "squid",
              "svn",
              "tomcat",
              "tss",
              "ups",
              "usbmuxd",
              "users",
              "utmp",
              "virt"]

    for group in groups:
        deleteGroup(group)

    users = ["apache",
             "avahi",
             "bitlbee",
             "clamav",
             "dhcp",
             "dialout",
             "dovecot",
             "ejabberd",
             "firebird",
             "gnokii",
             "hal",
             "icecast",
             "ldap",
             "mediatomb",
             "memcached",
             "mysql",
             "named",
             "nm-openconnect",
             "ntlmaps",
             "ntp",
             "openvpn",
             "oprofile",
             "partimag",
             "pnp",
             "postfix",
             "postgres",
             "pulse",
             "qemu",
             "quasselcore",
             "radiusd",
             "rtkit",
             "smmsp",
             "spamd",
             "squid",
             "svn",
             "tomcat",
             "tss",
             "ups",
             "usbmuxd",
             "vboxadd"]

    for user in users:
        deleteUser(user)

    # Merge new system groups
    # addGroup(gid, name)
    hav("addGroup", (30, "squid"))
    hav("addGroup", (50, "named"))
    hav("addGroup", (60, "mysql"))
    hav("addGroup", (70, "postgres"))
    hav("addGroup", (80, "apache"))
    hav("addGroup", (90, "dovecot"))
    hav("addGroup", (100, "users"))
    hav("addGroup", (102, "hal"))
    hav("addGroup", (104, "postfix"))
    hav("addGroup", (105, "postdrop"))
    hav("addGroup", (106, "smmsp"))
    hav("addGroup", (107, "locate"))
    hav("addGroup", (108, "utmp"))
    hav("addGroup", (109, "firebird"))
    hav("addGroup", (110, "dhcp"))
    hav("addGroup", (111, "ldap"))
    hav("addGroup", (112, "clamav"))
    hav("addGroup", (113, "ntlmaps"))
    hav("addGroup", (120, "avahi"))
    hav("addGroup", (123, "ntp"))
    hav("addGroup", (130, "tss"))
    hav("addGroup", (131, "ejabberd"))
    hav("addGroup", (132, "tomcat"))
    hav("addGroup", (133, "ups"))
    hav("addGroup", (134, "partimag"))
    hav("addGroup", (135, "radiusd"))
    hav("addGroup", (136, "oprofile"))
    hav("addGroup", (137, "mediatomb"))

    # 'pulse' is for system wide PA daemon.
    hav("addGroup", (138, "pulse"))

    # In order to access to a system wide PA daemon,
    # a user should be a member of the 'pulse-access' group.
    hav("addGroup", (139, "pulse-access"))

    hav("addGroup", (141, "italc"))
    hav("addGroup", (142, "quassel"))
    hav("addGroup", (143, "bitlbee"))
    hav("addGroup", (144, "icecast"))
    hav("addGroup", (145, "virt"))

    # Gnokii system user for the SMS daemon
    hav("addGroup", (146, "gnokii"))

    # Subversion
    hav("addGroup", (150, "svn"))

    # memcached
    hav("addGroup", (151, "memcached"))

    # For realtimeKit
    hav("addGroup", (152, "rtkit"))

    # NetworkManager user for OpenConnect VPN helper
    hav("addGroup", (153, "nm-openconnect"))

    # qemu & libvirtd
    hav("addGroup", (154, "qemu"))
    hav("addGroup", (155, "kvm"))

    # usbmuxd
    hav("addGroup", (160, "usbmuxd"))

    # OpenVPN
    hav("addGroup", (161, "openvpn"))

    # privoxy
    hav("addGroup", (162, "privoxy"))

    # Comar' profile groups
    hav("addGroup", (200, "pnp"))
    hav("addGroup", (201, "removable"))
    hav("addGroup", (202, "netuser"))
    hav("addGroup", (203, "netadmin"))
    hav("addGroup", (204, "power"))
    hav("addGroup", (205, "pnpadmin"))

    # Merge new system users
    # addUser(uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths)
    hav("addUser", (20, "dialout", "Dialout", "/dev/null", "/bin/false", "", ["dialout"], [], []))
    hav("addUser", (30, "squid", "Squid", "/var/cache/squid", "/bin/false", "", ["squid"], [], []))
    hav("addUser", (40, "named", "Bind", "/var/bind", "/bin/false", "", ["named"], [], []))
    hav("addUser", (60, "mysql", "MySQL", "/var/lib/mysql", "/bin/false", "", ["mysql"], [], []))
    hav("addUser", (70, "postgres", "PostgreSQL", "/var/lib/postgresql", "/bin/false", "", ["postgres"], [], []))
    hav("addUser", (80, "apache", "Apache", "/dev/null", "/bin/false", "", ["apache", "svn"], [], []))
    hav("addUser", (90, "dovecot", "Dovecot", "/dev/null", "/bin/false", "", ["dovecot"], [], []))
    hav("addUser", (102, "hal", "HAL", "/dev/null", "/bin/false", "", ["hal"], [], []))
    hav("addUser", (104, "postfix", "Postfix", "/var/spool/postfix", "/bin/false", "", ["postfix"], [], []))
    hav("addUser", (106, "smmsp", "smmsp", "/var/spool/mqueue", "/bin/false", "", ["smmsp"], [], []))
    hav("addUser", (109, "firebird", "Firebird", "/opt/firebird", "/bin/false", "", ["firebird"], [], []))
    hav("addUser", (110, "dhcp", "DHCP", "/dev/null", "/bin/false", "", ["dhcp"], [], []))
    hav("addUser", (111, "ldap", "OpenLDAP", "/dev/null", "/bin/false", "", ["ldap"], [], []))
    hav("addUser", (112, "clamav", "Clamav", "/dev/null", "/bin/false", "", ["clamav"], [], []))
    hav("addUser", (113, "ntlmaps", "NTLMaps", "/dev/null", "/bin/false", "", ["ntlmaps"], [], []))
    hav("addUser", (120, "avahi", "Avahi", "/dev/null", "/bin/false", "", ["avahi"], [], []))
    hav("addUser", (123, "ntp", "NTP", "/dev/null", "/bin/false", "", ["ntp"], [], []))
    hav("addUser", (130, "tss", "tss", "/var/lib/tpm", "/bin/false", "", ["tss"], [], []))
    hav("addUser", (131, "ejabberd", "Ejabberd", "/var/lib/ejabberd", "/bin/false", "", ["ejabberd"], [], []))
    hav("addUser", (132, "tomcat", "Tomcat", "/var/lib/tomcat", "/bin/false", "", ["tomcat"], [], []))
    hav("addUser", (133, "ups", "UPS", "/var/lib/nut", "/bin/false", "", ["ups", "dialout", "tty", "pnp"], [], []))
    hav("addUser", (134, "partimag", "Partimage", "/dev/null", "/bin/false", "", ["partimag"], [], []))
    hav("addUser", (135, "radiusd", "Freeradius", "/dev/null", "/bin/false", "", ["radiusd"], [], []))
    hav("addUser", (136, "oprofile", "oprofile", "/dev/null", "/bin/false", "", ["oprofile"], [], []))
    hav("addUser", (137, "mediatomb", "mediatomb", "/dev/null", "/bin/false", "", ["mediatomb"], [], []))
    hav("addUser", (138, "pulse", "PulseAudio System Daemon", "/var/run/pulse", "/bin/false", "", ["pulse", "pulse-access", "pulse-rt", "audio"], [], []))
    hav("addUser", (139, "quasselcore", "Quassel IRC System", "/var/cache/quassel", "/bin/false", "", ["quassel"], [], []))
    hav("addUser", (140, "bitlbee", "Bitlbee Gateway", "/var/lib/bitlbee", "/bin/false", "", ["bitlbee"], [], []))
    hav("addUser", (141, "spamd", "Spamassassin Daemon", "/var/lib/spamd", "/bin/false", "", [], [], []))
    hav("addUser", (145, "vboxadd", "VirtualBox Guest Additions", "/dev/null", "/bin/false", "", [], [], []))
    hav("addUser", (146, "gnokii", "Gnokii system user", "/", "/sbin/nologin", "", ["gnokii"], [], []))
    hav("addUser", (150, "svn", "Subversion", "/dev/null", "/bin/false", "", ["svn"], [], []))
    hav("addUser", (151, "icecast", "Icecast Server", "/dev/null", "/bin/false", "", ["icecast"], [], []))
    hav("addUser", (152, "memcached", "Memcached daemon", "/var/run/memcached", "/bin/false", "", ["memcached"], [], []))
    hav("addUser", (153, "rtkit", "RealtimeKit", "/proc", "/sbin/nologin", "", ["rtkit"], [], []))
    hav("addUser", (154, "nm-openconnect", "NetworkManager user for OpenConnect", "/", "/sbin/nologin", "", ["nm-openconnect"], [], []))
    hav("addUser", (155, "qemu", "QEMU", "/", "/sbin/nologin", "", ["qemu", "kvm"], [], []))
    hav("addUser", (160, "usbmuxd", "usbmuxd daemon", "/dev/null", "/bin/false", "", ["usbmuxd"], [], []))
    hav("addUser", (161, "openvpn", "OpenVPN", "/etc/openvpn", "/sbin/nologin", "", ["openvpn"], [], []))
    hav("addUser", (162, "privoxy", "Privoxy", "/etc/privoxy", "/sbin/nologin", "", ["privoxy"], [], []))

    # Comar' profile users
    hav("addUser", (200, "pnp", "PnP", "/dev/null", "/bin/false", "", ["pnp"], [], []))

    #migrate
    for u, g in migration:
        # setUser(uid, realname, homedir, shell, passwd, groups)
        hav("setUser", (u, "", "", "", "", g))

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
