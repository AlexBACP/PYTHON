# GUIA LISTAS
instructora= input("nombre de la intructora ")
edad_instructora= int(input("ingrese la edad de la instructora "))
alumnos =[]
edades= []

cantidad = int(input("cuantos estudiates son? "))
for i in range (cantidad):
     nombre= input(f"cual es tu nombre {i+1} ")
     alumnos.append(nombre)
     edad= int(input("cual es tu edad? "))
     edades.append(edad) 
print(f"""nombre de la instructora: {instructora} y tiene {edad_instructora} años,""")
for n,e in zip(alumnos, edades):
     print(f"""{n}, tiene {e} años""")


 #*************************************************************************************************************
 #aprendiz con la mayor edad
mayor= edades.index(max(edades))
print(f"El estudiante mayor es {alumnos[mayor]} con {edades[mayor]} años")

 #*************************************************************************************************************
 #estudiante/s con 18 años
ciertaEdad= [n for n,e in zip (alumnos, edades) if e==18]
print(f"Hay {len(ciertaEdad)} estudiantes con 18 años: ")
for est in ciertaEdad:
    print(est)

#*************************************************************************************************************
#
#eliminar nombre de la instructora
instructora = None   # o "" si prefieres dejarlo vacío
edad_instructora= None
print("\nLa instructora ha sido eliminada.")
#*************************************************************************************************************
#indicar un dato dentro de la lista
dato= input("digite el nombre que quiere buscar en la lista ")

if dato in alumnos:
     indice= alumnos.index(dato)
     print(f"{dato} esta en la lista y tiene {edades[indice]} años.")
else:
     print(f"{dato} no se encuentra en la lista de aprendices.")

#*************************************************************************************************************
#buscar elementos con el indice
inicio=int(input("ingrese el indice inicial: "))
fin=int(input("ingrese el indice final: "))
print("\n Estudiantes en ese rango ")
for i in range(inicio, fin):
    print(f"Índice {i}: {alumnos[i]}, {edades[i]} años")

#*************************************************************************************************************
#estudiantes con indice par
print("\n--- Estudiantes con índice par ---")
for indice, (nombre, edad) in enumerate(zip(alumnos, edades)):
    if indice % 2 == 0:  # condición: índice par
        print(f"Índice {indice}: {nombre}, {edad} años")
    

    
