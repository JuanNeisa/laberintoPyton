archivo = open("prueba1.txt", "r")
for linea in archivo.readlines():
    print(linea)
    
archivo.close() 
