#Taidy Johana Marrugo Simancas
# Estudiante MISO- 201510455
print("Knuth Vol 2 Algorithm B")
try:
    xo = int(raw_input("Ingrese el valor de xo ")) # valor ingresado por consola
except ValueError:
    xo = 0#seed (x0) = parametro, default 0, en caso de no ingresar.
try:
    k = int(raw_input("Ingrese el valor de k "))# valor ingresado por consola
except ValueError:
    k =1000000 # parametro, default 10 potencia 6, en caso de no ingresar.
m = 256
a = 16807
c = 1234
n = 100 #numero de bytes aleatorios por retornar, default 100
vector = []
vector.append(xo)
for x in range(1, k):
    temporal = xo
    valor_posicion_vector = (a * temporal + c) % m
    vector.append(valor_posicion_vector)
    xo = valor_posicion_vector
print("vector inicial con PRNG ")
print(vector)
print("valores para calcular Y:\na= "+str(a)+"\nXsub(k-1)=vector[k - 1] = "+str(vector[k - 1])+"\nc= "+str(c)+"\nm="+str(m))
y = ((a * vector[k - 1]) + c) % m
print("Valor de Y= (aXsub(k-1)+c)mod m =" + str(y))
j = (k * y) / m
print("valor de j=[ky/m] =" + str(j))
y = vector[j]
print("Better Random Number  y= V [j]= " + str(y))
