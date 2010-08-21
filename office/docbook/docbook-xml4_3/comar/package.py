#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/build-docbook-catalog")
    os.system('/usr/bin/install-catalog --add "/etc/sgml/xml-docbook-4.3.cat" \
               "/etc/sgml/sgml-docbook.cat"')
    os.system('/usr/bin/install-catalog --add "/etc/sgml/xml-docbook-4.3.cat" \
               "/usr/share/sgml/docbook/xml-dtd-4.3/docbook.cat"')

def preRemove():
    os.system('/usr/bin/install-catalog --remove "/etc/sgml/xml-docbook-4.3.cat" \
               "/etc/sgml/sgml-docbook.cat"')
    os.system('/usr/bin/install-catalog --remove "/etc/sgml/xml-docbook-4.3.cat" \
               "/usr/share/sgml/docbook/xml-dtd-4.3/docbook.cat"')
