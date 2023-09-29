"""Creacion del diccionario"""
peliculas = {"David Yates":"Harry Potter", 
             "Anthony Russo":"Avengers Endgame",
             "Matt Reeves":"The Batman",
             "Todd Phillips":"Joker"}

"""Imprimir nombre de los directores"""
print("Directores: ")
#print(peliculas.keys())
for clave in peliculas.keys():
    print(clave," | ", end = " ")
print()
print()
    
"""Adicionar la pelicula Toy Story con director Lee Unkrich
e imprimir diccionario"""
peliculas["Lee Unkrich"] = "Toy Story"
print("Peliculas: ")
for clave, valor in peliculas.items():
    print(f'{clave}: {valor}')
print()
 
"""Pedir el nombre del director y borrarlo del diccionario"""
nombreDirector = input("Nombre del director a eliminar: ")
if nombreDirector in peliculas:
    peliculas.pop(nombreDirector.title())
else:
    print('El director no existe')
    
for clave, valor in peliculas.items():
    print(f'{clave}: {valor}')
print()

""""""