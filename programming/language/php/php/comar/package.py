import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    module_enable('PHP5')

def preRemove():
    module_disable('PHP5')

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
