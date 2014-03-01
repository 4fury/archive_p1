#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.cflags.add("-fPIC")
    pisitools.cxxflags.add("-fPIC")
    pisitools.ldflags.add("-fPIC")
    autotools.autoreconf("-f")
    autotools.configure("--prefix=/usr")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("*txt")
