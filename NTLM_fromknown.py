#!/usr/bin/python

import itertools as it,hashlib,binascii
pw = 'password'
per = list(it.combinations_with_replacement('1234567890-=`!@#$%^&*()_+,./<>?;:"[]{}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',3))
for x in per:
	t1 = ''.join(x)
	intstr = pw + t1
	ntlmhash = binascii.hexlify(hashlib.new('md4', intstr.encode('utf-16le')).digest())
	print pw + t1 + "	" + ntlmhash 
