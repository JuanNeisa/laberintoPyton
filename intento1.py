
def leer_archivo(direccion):
	return [x.split(" ") for x in [y.strip("\n") for y in open(direccion).readlines()]][:-2]
def coor_inicial(direccion, tamaño):
	return [x.split(",") for x in [y.strip("\n") for y in open(direccion).readlines()]][tamaño:][:-1]
def coor_final(direccion, tamaño):
	return [x.split(",") for x in [y.strip("\n") for y in open(direccion).readlines()]][(tamaño + 1):]
def tamaño_listas(x):
    return len(x)

print (tamaño_listas(leer_archivo('prueba1.txt')))
print(coor_inicial('prueba1.txt' , tamaño_listas(leer_archivo('prueba1.txt'))))
print(coor_final('prueba1.txt', tamaño_listas(leer_archivo('prueba1.txt'))))
