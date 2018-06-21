# generica
import hashlib

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