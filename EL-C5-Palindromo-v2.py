lista = []
cadena = input("Ingrese la cadena a verificar: ")
lista = list(cadena)
listaInv = lista[:]
listaInv.reverse()

if lista == listaInv:
    print("La palabra es un Palíndromo")
else:
    print ("No es un Palíndromo ")
    print("Cadena: ",lista,"| Cadena invertida: ",listaInv)