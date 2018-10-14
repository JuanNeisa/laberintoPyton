def cargar_archivo(archivo):
    return [y.split(" ") for y in [x.strip("\n") for x in open(archivo).readlines()]]

def laberinto(archivo):
    return cargar_archivo(archivo)[:-2]

def coordenadas_inicio(archivo):
    return cargar_archivo(archivo)[-2][0].split(",")

def coordenadas_fin(archivo):
    return cargar_archivo(archivo)[-1][0].split(",")

def x(lista, numero):
    return int(lista[numero])

def c(lab,inicio):
    if(lab[x(inicio,0)][x(inicio,1)] == '1'):
        return "Paila"
    else:
        return "yeeu"
        
    

print (laberinto("prueba1.txt"))

print (coordenadas_inicio("prueba1.txt"))

print (coordenadas_fin("prueba1.txt"))

print (c(laberinto("prueba1.txt"), coordenadas_inicio("prueba1.txt")))

