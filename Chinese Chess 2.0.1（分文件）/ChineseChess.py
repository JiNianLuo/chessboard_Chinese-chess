#!/usr/bin/env python
import os
import sys

if sys.version_info[0] > 2:
    print("This game runs on python 2 only")

try:
    from ChessLib.UI import display
    display()
except ImportError:
    print "The version of Tcl/Tk in use may be unstable.\n Visit http://www.python.org/downloads/ for current information."
