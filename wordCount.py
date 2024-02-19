#! /usr/bin/env python3


import os
import re
import stat
from sys import argv



inf = argv[1]
outp = argv[2]
sbuff = ""
fdi = os.open(inf, os.O_RDONLY, stat.S_IRWXU )
assert fdi >=0
ibuff = os.read(fdi, 100)
while len (ibuff):
    sbuff = sbuff + ibuff.decode()
    ibuff = os.read(fdi, 100)
os.write(1, sbuff.encode())