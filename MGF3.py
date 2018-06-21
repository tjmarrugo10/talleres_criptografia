#Taidy Johana Marrugo Simancas
# Estudiante MISO- 201510455
import math
import hashlib
from binascii import hexlify
from hashlib import sha256
from hashlib import sha1
print("Algoritmo de ciframiento de flujo basado en Algoritmo B - Randomizing by shuffling y a Mask Generation Function (RFC 2437)")
xo = 0#semilla de la congruencia lineal, valor inicial, a efectos practicos la clave. Valor por defecto 0
k =1000000 #tamanio del vector del Algoritmo B. Valor por defecto 1000000
m = 256 #modulo de la congruencia lineal. Valor por defecto 256
a = 16807 #constante de la congruencia lineal. Valor por defecto 16807
c = 1234 #constante de la congruencia lineal. Valor por defecto 1234
M="Shhhh, super-secreto."
vector = []
vector.append(xo)
for x in range(1, k):
    temporal = xo
    valor_posicion_vector = (a * temporal + c) % m
    vector.append(valor_posicion_vector)
    xo = valor_posicion_vector
#print("vector inicial con PRNG ")
#print(vector)
#print("valores para calcular Y:\na= "+str(a)+"\nXsub(k-1)=vector[k - 1] = "+str(vector[k - 1])+"\nc= "+str(c)+"\nm="+str(m))
y = ((a * vector[k - 1]) + c) % m
#print("Valor de Y= (aXsub(k-1)+c)mod m =" + str(y))
j = (k * y) / m
#print("valor de j=[ky/m] =" + str(j))
y = vector[j]
print("Better Random Number  y= V [j]= " + str(y))
print ("inicio del calculo de n =piso de la raiz cuadrada de la longitud del mensaje M")
n=int(math.sqrt(len(M)))#inicio del calculo de n =piso de la raiz cuadrada de la longitud del mensaje M
print(str(n))
z=n#numero aleatorio de n Bytes de largo, utilicelo como semilla Z de la MGF1
def i2osp(integer, size=4):
    return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(size))])#generacion una secuencia aleatoria S de Bytes delength(M) de largo.


def mgf1(input, length, hash=hashlib.sha1):
    counter = 0
    output = ''
    while (len(output) < length):
        C = i2osp(counter, 4)
        output += hash(input + C).digest()
        counter += 1
    return output[:length]


print "MGF1"
print hexlify(mgf1(M, len(M), sha1))#recibe el texto M, length(M) de largo y tipo de cifrado

