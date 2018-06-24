#Taidy Johana Marrugo Simancas
# Estudiante MISO- 201510455
import math
import hashlib
from binascii import hexlify
from hashlib import sha1
import binascii
import sys
import struct

print("Algoritmo de ciframiento de flujo basado en Algoritmo B - Randomizing by shuffling y a Mask Generation Function (RFC 2437)")
try:
    xo = int(raw_input("Ingrese el valor de xo ")) # valor ingresado por consola
except ValueError:
    xo = 0#semilla de la congruencia lineal, valor inicial, a efectos practicos la clave. Valor por defecto 0
try:
    k=int(raw_input("Ingrese el valor de k "))
except  ValueError:
    k =1000000 #tamanio del vector del Algoritmo B. Valor por defecto 1000000
try:
    m=int(raw_input("Ingrese el valor de m "))
except ValueError:
    m = 256 #modulo de la congruencia lineal. Valor por defecto 256
try:
    a=int(raw_input("Ingrese el valor de a "))
except ValueError:
    a = 16807 #constante de la congruencia lineal. Valor por defecto 16807
try:
    c=int(raw_input("Ingrese el valor de c "))
except ValueError:
    c = 1234 #constante de la congruencia lineal. Valor por defecto 1234

M=raw_input("Ingrese el texto ")
if not M:
    M = "Shhhh, super-secreto."  # texto claro, string, valor por defecto



vector = []#vector para numeros aleatorios inicial
vector.append(xo)
for x in range(1, k):
    temporal = xo
    valor_posicion_vector = (a * temporal + c) % m
    vector.append(valor_posicion_vector)
    xo = valor_posicion_vector
#print("vector inicial con PRNG ")
#print(vector)
vector_bytes=[];
n=int(math.sqrt(len(M)))#n Bytes de largo
print("n (piso de la raiz cuadrada de la longitud del mensaje M) de bytes de largo a utilizar para encontrar los n elemento  en el vector de tamanio "+str(k)+" :  "+str(n))
for j in range(0,n):
    vector_bytes.append(vector[j])
print("vector de n bytes: "+str(vector_bytes))
bytesToHex=""
for l in range(0,n):
    print("byte " +str(vector_bytes[l])+" convertido a hex "+ binascii.hexlify(str(vector_bytes[l])))
    bytesToHex+=binascii.hexlify(str(vector_bytes[l]))
print("vector de bytes convertido a HEX: "+bytesToHex)


Z=bytesToHex#semilla Z de la MGF1
print("valor de Z para GMF1: "+Z)
#inicio de GMF1
def i2osp(integer, size=4):
    return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(size))])#generacion una secuencia aleatoria S de Bytes delength(M) de largo.

def mgf1(input, length, hash=hashlib.sha1):#algoritmo
    counter = 0
    output = ''
    while (len(output) < length):
        C = i2osp(counter, 4)
        output += hash(input + C).digest()
        counter += 1
    return output[:length]
#fin de GMF1
#operacion XOR con 2 hex
def xor_strings(mhex, shex):

    """
    xor two strings together by first getting their ascii code values
    and then xor'ing them
    """
    # ord returns an integer of the ascii code of a given one char string
    # chr returns a one char string from a given ascii code value
    # hexlify turns the given string into a hex string
    #return (''.join(chr(ord(a)^ord(b)) for a, b in zip(mhex, shex)))
    if len(mhex) > len(shex):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(mhex[:len(shex)], shex)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(mhex, shex[:len(mhex)])])

print "RESULTADO DE MGF1"
shex=hexlify(mgf1(Z, len(M), sha1))#recibe la semilla Z, length(M) de largo y tipo de cifrado
print ("secuencia aleatoria S de Bytes de length(M) de largo: "+shex )
mhex=hexlify(M)#convertir M en hexagesimal
print("Texto M en hex: "+mhex)
C=xor_strings(mhex,shex)#RESULTADO DE C, CIFRADO
print "Mensaje Cifrado C=M XOR S: "+C
descifrado=xor_strings(C,shex)
print "Mensaje descifrado M=C XOR S en HEX: "+descifrado# RESULTADO DE M, DESCIFRADO
print "Mensaje descifrado M=C XOR S: "+binascii.unhexlify(descifrado)# RESULTADO DE M, DESCIFRADO

