#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "Unidecode-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def check():
    pythonmodules.compile("test")

def install():
    pythonmodules.install()

