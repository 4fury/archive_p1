#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "PasteDeploy-%s" % get.srcVERSION()

def install():
    pythonmodules.install()
    pisitools.insinto("%s/%s/" % (get.docDIR(), get.srcNAME()), "docs/*")
