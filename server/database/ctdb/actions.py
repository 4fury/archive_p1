#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")

    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE -DCTDB_VERS=\"%s\"" % (get.CFLAGS(), get.srcVERSION()))
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/var/run/ctdb","/run")
    pisitools.removeDir("/var/run")
    pisitools.dodoc("COPYING","README","NEWS")
