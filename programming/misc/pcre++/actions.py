#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # use CXXFLAGS from environment
    pisitools.dosed("libpcre++/Makefile.am", "^CXXFLAGS.*", "")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("%s/usr/doc/libpcre++-%s/*" % (get.installDIR(),get.srcVERSION()))
    pisitools.removeDir("/usr/doc")
