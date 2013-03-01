#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move docs into proper place
    pisitools.domove("/usr/share/libatomic_ops/", "/usr/share/doc/%s" % get.srcNAME())

    pisitools.remove("/usr/include/atomic_ops/sysdeps/README")
