#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.am", "win32 ", "")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-assert \
                         --enable-pcsc \
                         --with-pcsc-provider=libpcsclite.so.1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc", "etc/opensc.conf")

    pisitools.dodoc("README")
