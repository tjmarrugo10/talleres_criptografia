#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from binascii import hexlify
from hashlib import sha256
from hashlib import sha1
#de la guia de la ppt
def i2osp(integer, size=4):
  return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(size))])

def mgf1(input, length, hash=hashlib.sha1):
  counter = 0
  output = ''
  while (len(output) < length):
    C = i2osp(counter, 4)
    output += hash(input + C).digest()
    counter += 1
  return output[:length]

salida = False
while not salida:
	print "MGF1"
	z = 4
	l = 21
	print hexlify(mgf1("Shhhh, super-secreto.", l, sha256))
	print hexlify(mgf1("Shhhh, super-secreto.", l, sha1))
	respuesta = int(input("Salir <1. Si - 2. No> : "))
	salida = True if respuesta == 1 else False
#end while
	
