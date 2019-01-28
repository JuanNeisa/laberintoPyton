def getArchivo():
    return "prueba1.txt"

def cargar_archivo(archivo):
    return [x for x in open(archivo).readlines()]

def laberinto(archivo):
    return cargar_archivo(archivo)[:-2]

def c_inicio(archivo):
    return [y.split(" ") for y in [x.strip("\n") for x in open(archivo).readlines()]][-2][0].split(",")

def creaLaberinto(stringLab):

    lista = stringLab.split()
    lista = [ x[:-1] if x[-1] == "\n" else x for x in lista]
    lista = [[int(ch) for ch in x] for x in lista]
    return lista
 
def impLab(laberinto):
         
    for x in laberinto:
        for y in x:
            print(y, end= "")
        print()
        
laberinto = creaLaberinto("".join(laberinto(getArchivo())))
impLab(laberinto)

def recorrido(i, j):
    
    if laberinto[i][j] == 3:
        return [(i, j)]
 
    if laberinto[i][j] == 1:
        return []
 

    laberinto[i][j] = 1
 
    if i > 0 and laberinto[i - 1][j] in [0, 3]:                     # Arriba
        camino = recorrido(i - 1, j)
        if camino: return [(i, j)] + camino
 
    if j < len(laberinto[i]) - 1 and laberinto[i][j + 1] in [0, 3]: # Este
        camino = recorrido(i, j + 1)
        if camino: return [(i, j)] + camino
 
    if i < len(laberinto) - 1 and laberinto[i + 1][j] in [0, 3]:    # Abajo
        camino = recorrido(i + 1, j)
        if camino: return [(i, j)] + camino
 
    if j > 0 and laberinto[i][j - 1] in [0, 3]:                     # Oeste
        camino = recorrido(i, j - 1) 
        if camino: return [(i, j)] + camino
 
    return []
    

##for x in recorrido(int(c_inicio(getArchivo())[0]),int(c_inicio(getArchivo())[1])) : print(x)
if(recorrido(int(c_inicio(getArchivo())[0]),int(c_inicio(getArchivo())[1])) == []):
    print("Sin solucion")
else:
    print("Con solucion")
