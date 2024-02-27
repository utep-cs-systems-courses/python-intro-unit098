#! /usr/bin/env python3


import os
import re
import stat
import string
from sys import argv


if len(argv)!=3:
    os.write(2, "Correct usage: wordCount.py <infile> <outfile>\n".encode())
elif not os.path.exists(argv[1]):
    os.write(2, "Infile does not exist\n".encode())
else:
    inf = argv[1]
    outp = argv[2]
    sbuff = ""
    outwrd = ""
    fdi = os.open(inf, os.O_RDONLY, stat.S_IRWXU )
    assert fdi >=0
    ibuff = os.read(fdi, 100)
    while len (ibuff):
        sbuff = sbuff + ibuff.decode()
        ibuff = os.read(fdi, 100)
    sbuff = sbuff.lower()
    sbuff = re.sub(",|\.|;|:|\"|", '',  sbuff)
    wordsl = re.split(" |\n|-|'", sbuff)
    wordsd = dict()
    for word in wordsl:
        if word in wordsd:
            wordsd[word] += 1
        else:
            wordsd[word] = 1
            
    wordsd.pop('')
    wordso = list(wordsd.keys())
    wordso.sort()
    for key in wordso:
        outwrd += key+" " + str(wordsd[key])+"\n"
    fd3 = os.open(outp, os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
    outbb = outwrd.encode()
    btw = len(outbb)
    while btw:
        nb = os.write(fd3, outbb)
        btw -= nb
        outbb=outbb[nb::]
    