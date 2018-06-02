import shutil
from shutil import copytree, ignore_patterns
import os
import errno
import pipeit
import pipeui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


#version .002 adding class a base ui
#ultraMove For moving files from one place to the other and doing other fancy stuff.
#


#src = "C:\\sandbox\\source"
#dst = "C:\\sandbox\\target"




src = os.listdir("C:\\sandbox\\source")
dst = "C:\\sandbox\\target"
for files in src:
    if files.endswith(".txt"):
        shutil.copy(files,dst)

def ultraCopyTree(src, dst, ignore=ignore_patterns('*.pyc', 'tmp*')):
 copytree(src, dst, ignore=ignore_patterns('*.pyc', 'tmp*'))
ultraCopyTree(src,dst,ignore=ignore_patterns('*.pyc', 'tmp*'))
pipeit.ultraShout("you")
# Directories are the same
#source = "C:\\sandbox\\source'
#destination = 'C:\\sandbox\\target'
#ignored=""

#ultraCopy(source,destination,ignored)
