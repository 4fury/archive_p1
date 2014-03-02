#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.system("ant build")

def install():
    pisitools.insinto("/usr/share/java/", "ecj.jar", "eclipse-ecj-4.3.2.jar")
    shelltools.cd("%s/usr/share/java/" % get.installDIR())
    pisitools.dosym("eclipse-ecj-4.3.2.jar", "/usr/share/java/ecj.jar")
    pisitools.dosym("eclipse-ecj-4.3.2.jar", "/usr/share/java/eclipse-ecj.jar")
