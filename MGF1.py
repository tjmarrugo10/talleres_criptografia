#Taidy Johana Marrugo Simancas
# Estudiante MISO- 201510455
import math
import hashlib
from binascii import hexlify
from hashlib import sha1
import binascii
import sys

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



vector = []#vector para numeros aleatorios
vector.append(xo)
for x in range(1, k):
    temporal = xo
    valor_posicion_vector = (a * temporal + c) % m
    vector.append(valor_posicion_vector)
    xo = valor_posicion_vector
#print("vector inicial con PRNG ")
#print(vector)
#print("valores para calcular Y en vector inicial : \na= "+str(a)+"\nXsub(k-1)=vector[k - 1] = "+str(vector[k - 1])+"\nc= "+str(c)+"\nm="+str(m))
y = ((a * vector[k - 1]) + c) % m
#print("Valor de Y en vector inicial = (aXsub(k-1)+c)mod m =" + str(y))
j = (k * y) / m
#print("valor de j en vector inicial =[ky/m] =" + str(j))
y = vector[j]
#print("Better Random Number  y= V [j]= en vector inicial " + str(y))
n=int(math.sqrt(len(M)))#n Bytes de largo
print("n (piso de la raiz cuadrada de la longitud del mensaje M) de bytes de largo a utilizar para encontrar el aleatorio en el vector de tamanio 1000000:  "+str(n))
z=0#semilla Z de la MGF1
for x in range(0,k):#buscar en el vector aleatorio un byte que tenga #n Bytes de largo
    bytesByNumberOfVector=sys.getsizeof(vector[x]);#obtengo los bytes por cada numero aleatorio del vector
    if bytesByNumberOfVector == n:
        print("bytesByNumberOfVector "+str(bytesByNumberOfVector))
        print("position of bytesByNumberOfVector "+str(x))
        z=vector[x]#numero aleatorio de n Bytes de largo, utilicelo como semilla Z de la MGF1.# del vector sacar un numero aleatorio de n Bytes de largo
        break;
print("valor de z para GMF1: "+str(z))
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

def xor_strings(mhex, shex):
    """
    xor two strings together by first getting their ascii code values
    and then xor'ing them
    """
    # ord returns an integer of the ascii code of a given one char string
    # chr returns a one char string from a given ascii code value
    # hexlify turns the given string into a hex string
    return hexlify(''.join(chr(ord(a)^ord(b)) for a, b in zip(mhex, shex)))

print "MGF1"
shex=hexlify(mgf1(M, len(M), sha1))#recibe el texto M, length(M) de largo y tipo de cifrado
print ("secuencia aleatoria S de Bytes delength(M) de largo: "+shex)
mhex=binascii.hexlify(M)#convertir M en hexagesimal
print("Texto M en hex: "+mhex)
C=xor_strings(mhex,shex)#RESULTADO DE C, CIFRADO
print "C=M XOR S: "+C
print "M=C XOR S: "+xor_strings(binascii.hexlify(C),shex)# RESULTADO DE M, DESCIFRADO

