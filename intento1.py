"""archivo = open("prueba1.txt", "r")
for linea in archivo.readlines():
    print(linea)
    
archivo.close() 

def
#def mirarLista():
    #variable= "hola mundo hallo welt"
   # print("hola mundo hallo welt".split())


#mirarLista()
"""

def cargar_archivo(archivo):
    return [y.split(" ") for y in [x.strip("\n") for x in open(archivo).readlines()]]

def laberinto(archivo):
    return cargar_archivo(archivo)[:-2]

def coordenadas_inicio(archivo):
    return cargar_archivo(archivo)[-2][0].split(",")

def coordenadas_fin(archivo):
    return cargar_archivo(archivo)[-1][0].split(",")


print laberinto("prueba1.txt")

print coordenadas_inicio("prueba1.txt")

print coordenadas_fin("prueba1.txt")
