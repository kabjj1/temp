#!/usr/bin/python

import itertools as it,hashlib,binascii
pw = 'password'
per = list(it.combinations_with_replacement('12345$
for x in per:
        t1 = ''.join(x)
        intstr = pw + t1
        ntlmhash = binascii.hexlify(hashlib.new('m$
        print pw + t1 + "       " + ntlmhash 
