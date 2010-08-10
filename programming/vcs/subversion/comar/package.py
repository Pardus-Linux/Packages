#!/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    module_enable('SVN')
    module_enable('SVN_AUTHZ')
    os.system("/bin/mkdir -p /var/svn/repos/default")
    os.system("/usr/bin/svnadmin create /var/svn/repos/default")
    os.system("/bin/chown -Rf svn:svn /var/svn")
    os.system("/bin/chmod -Rf 774 /var/svn/repos")
    os.system("/bin/chmod 775 /var/svn/repos")

def preRemove():
    module_disable('SVN')
    module_disable('SVN_AUTHZ')

def module_enable(mod):
    s = open('/etc/conf.d/apache2').read()
    modules = [i.strip() for i in re.findall('APACHE2_OPTS="(.*)"',  s)[0].split('-D') if i.strip()]

    if mod not in modules:
        s2 = re.sub('APACHE2_OPTS="(.*)"', 'APACHE2_OPTS="\\1 -D %s"' % mod, s)
        open('/etc/conf.d/apache2', 'w').write(s2)
        return True

    return False

def module_disable(mod):
    s = open('/etc/conf.d/apache2').read()
    modules = [i.strip() for i in re.findall('APACHE2_OPTS="(.*)"',  s)[0].split('-D') if i.strip()]

    if mod in modules:
        modules.remove(mod)
        mods = ' '.join(['-D %s' % i for i in modules])
        s2 = re.sub('APACHE2_OPTS="(.*)"', 'APACHE2_OPTS="%s"' % mods, s)
        open('/etc/conf.d/apache2', 'w').write(s2)
        return True

    return False
