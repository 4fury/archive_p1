#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("dstat")

    pisitools.insinto("/usr/share/dstat", "plugins/*.py")

    pisitools.doman("docs/dstat.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "TODO", "examples/mstat.py", "examples/read.py")
