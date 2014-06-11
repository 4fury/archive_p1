#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DOGRE_INSTALL_SAMPLES=TRUE \
                          -DOGRE_INSTALL_DOCS=TRUE \
                          -DOGRE_INSTALL_SAMPLES_SOURCE=TRUE \
                          -DOGRE_FULL_RPATH=0 \
                          -DCMAKE_SKIP_RPATH=1 \
                          -DOGRE_LIB_DIRECTORY=lib \
                          -DOGRE_BUILD_RTSHADERSYSTEM_EXT_SHADERS=1 \
                          -DOGRE_BUILD_PLUGIN_CG=0")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("Docs/*.html")
    pisitools.dohtml("Docs/*.gif")


    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", \
                    "README", "Docs/shadows/OgreShadows.pdf", \
                    "Docs/licenses/*.txt")
