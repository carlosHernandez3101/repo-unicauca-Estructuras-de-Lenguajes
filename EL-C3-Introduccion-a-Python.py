#Comentario de una sola linea
"""Comentario de varias lineas"""

print("Ejemplo de concatenacion: ")
nombre, salario = "Gaby", 5000000
print("la Señorita ", nombre, " se gana ", salario, " mensualmente")
print("")

print("Imprimir numeros del 1 al 10: ")
i = 0
while i < 10:
    i = i + 1
    print(i)
print("")
for i in range(10):
    print(i)
print("")
    
#Ejercicio imprimir impares    
print("Numeros impares: ")
for i in range(1,10,2):
    print(i)
print("")

"""Ejercicio imprimir utilizando JKLMNOPQ y para cada letra
concatenarle 'ack' ejemplo: Jack Kack Lack """
for i in range(74, 82, 1):
    print(chr(i)+"ack")

for i in ('JKLMNOPQ'):
    print(i + "ack")
print("")

""" print("Ejercicio para conocer el numero central de tres numeros diferentes")
medio = 0
a = int(input("Ingrese el primer numero: "))

b = int(input("Ingrese el segundo numero: "))
while a == b:
    print ("El segundo numero debe ser diferente del primero")
    b = int(input("Ingrese el segundo numero: "))

c = int(input("Ingrese el tercer numero: "))
while a == c or b == c:
    print ("El tercer numero debe ser diferente del primero y/o del segindo")
    c = int(input("Ingrese el tercer numero: "))

if (a > b and a < c) or (a < b and a > c):
    print("El numero central es ", a)
elif (b > a and b < c) or (b < a and b > c):
    print("El numero central es ", b)
else:
    print("El numero central es ", c)
print("")
#Version mas optima
menor = min(a, b, c)
mayor = max(a, b, c)
central = (a + b + c) - menor - mayor
print("El numero central es ", central) 
print("")"""

print("Ejercicio de conteo de vocales")
vocales = 'aeiou'
palabra = input("Ingrese una palabra: ")
contVocales = 0
for i in (palabra):
    if i.lower() in vocales:
        contVocales += 1

print("La palabra ", palabra, " tiene ", contVocales, " vocales. " )

