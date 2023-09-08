cadena = "Peru"

listCadena = list(cadena)

cadenaInvertida = listCadena[::-1]

if(listCadena == cadenaInvertida):
    print("La palabra es un Palíndromo")
else:
    print ("No es un Palíndromo ")
    print("Cadena: ",listCadena,"| Cadena invertida: ",cadenaInvertida)