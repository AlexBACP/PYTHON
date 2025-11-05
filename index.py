
"""A un empleado le aplican una retención del 18% sobre su salario básico, y le entregan una
Bonificación de 1.3% sobre el salario. Desarrolle un algoritmo que permita calcular e
imprimir el salario neto y los valores de sus respectivos porcentajes.
 Definición de la función para calcular el salario neto
 Solicitar el salario básico"""

#pedimos el salario básico al usuario
salario_basico = float(input("Ingrese el salario básico del empleado: "))

# Cálculo de retención, bonificación y salario neto
retencion = salario_basico * 0.18
bonificacion = salario_basico * 0.013
salario_neto = salario_basico - retencion + bonificacion
# Impresión de resultados
print(
    f"Salario básico: ${salario_basico:.2f}\n"
    f"Retención (18%): ${retencion:.2f}\n"
    f"Bonificación (1.3%): ${bonificacion:.2f}\n"
    f"Salario neto: ${salario_neto:.2f}"
)

"""Una cancha de futbol fue ampliada en un 20%. Determinar el área total en metros de la
cancha."""

#pedimos las dimensiones originales de la cancha al usuario
largo_original = float(input("Ingrese el largo original de la cancha en metros: "))
ancho_original = float(input("Ingrese el ancho original de la cancha en metros: "))

# Cálculo del área original y el área ampliada
area_original = largo_original * ancho_original 
area_ampliada = area_original * 1.2
# Impresión del área total ampliada
print(f"El área total ampliada de la cancha es: {area_ampliada:.2f} metros cuadrados")

"""El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
trimestre cayó en un 1.5%. Calcular el valor del desempleo actual."""

#el valor de desempleo en ibague durante el primer trimestre generalmente esta entre un 15,0%,
#en el segundo trimestre suele estar en 13,5%, en el tercero desciende a 12,8%,
#por lo que podemos calcular que en el cuarto trimestre...

# Cálculo del desempleo actual en Ibagué en este trimestre
# Datos conocidos:
desempleo_inicial = 10.0    
primer_trimestre = 9.5      
segundo_trimestre = 1.5 

# Cálculo paso a paso
despues_primer = desempleo_inicial * (1 + primer_trimestre / 100)
desempleo_actual = despues_primer * (1 - segundo_trimestre / 100)

# Mostrar resultados
print("Tasa de desempleo en Ibagué:")
print(f"- Inicial: {desempleo_inicial:.2f}%")
print(f"- Después del primer trimestre (+{primer_trimestre}%): {despues_primer:.2f}%")
print(f"- Después del segundo trimestre (-{segundo_trimestre}%): {desempleo_actual:.2f}%")
print(f"El valor actual del desempleo en Ibagué es: {desempleo_actual:.2f}%")


"""Calcular el área total de un terreno en metros sabiendo que esta fue reducida en un 10%,
y posteriormente, le fue adicionado un 50% con relación al área después de la reducción.
"""
# Datos
area_inicial = 1000  # m²
reduccion = 10      
aumento = 50         

# Cálculo
area_despues_reduccion = area_inicial * (1 - reduccion / 100)
area_final = area_despues_reduccion * (1 + aumento / 100)

# Resultado
print(f"Área inicial: {area_inicial} m²")
print(f"Área después de la reducción: {area_despues_reduccion:.2f} m²")
print(f"Área final: {area_final:.2f} m²")


"""Hacer un algoritmo que permita determinar las horas a las que equivale una cantidad de
minutos ingresados por el usuario."""

# Solicitar los minutos al usuario
minutos = int(input("Ingrese la cantidad de minutos: "))

# Calcular horas y minutos restantes
horas = minutos // 60         # División entera para obtener horas completas
minutos_restantes = minutos % 60  # Módulo para obtener los minutos que sobran

# Mostrar resultados
print("\n--- Conversión ---")
print(f"{minutos} minutos equivalen a:")
print(f"{horas} hora(s) y {minutos_restantes} minuto(s)")

"""Desarrollar un algoritmo que permita convertir de quintal a kilogramos, tenga en cuenta
que un quintal equivale a 100 kilogramos."""

# Solicitar la cantidad de quintales al usuario
quintales = float(input("Ingrese la cantidad de quintales: "))

# Convertir a kilogramos
kilogramos = quintales * 100

# Mostrar el resultado
print(f"\n{quintales} quintal(es) equivalen a {kilogramos} kilogramos.")

"""Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
llamadas a cada operador, y el total de las cuatro llamadas."""

# Solicitar los costos de las llamadas
print("Ingrese los costos de las llamadas al primer operador:")
llamada1_op1 = float(input("Costo de la primera llamada: "))
llamada2_op1 = float(input("Costo de la segunda llamada: "))

print("\nIngrese los costos de las llamadas al segundo operador:")
llamada1_op2 = float(input("Costo de la primera llamada: "))
llamada2_op2 = float(input("Costo de la segunda llamada: "))

# Calcular totales por operador
total_op1 = llamada1_op1 + llamada2_op1
total_op2 = llamada1_op2 + llamada2_op2

# Calcular total general
total_general = total_op1 + total_op2

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Llamadas al primer operador: ${llamada1_op1:.2f}, ${llamada2_op1:.2f}")
print(f"Total primer operador: ${total_op1:.2f}")

print(f"Llamadas al segundo operador: ${llamada1_op2:.2f}, ${llamada2_op2:.2f}")
print(f"Total segundo operador: ${total_op2:.2f}")

print(f"Total de las cuatro llamadas: ${total_general:.2f}")


"""El propietario de una vivienda necesita renovar parte de esta, para lo cual tiene planeado
enchapar los muros de los baños. La persona responsable de hacer este trabajo mide el
alto y ancho de los muros. Se pide realizar un algoritmo para calcular el área del baño y el
número de baldosas necesarios para cubrir el baño. Sabiendo que la caja trae 3.5 metros
cuadrados."""

# Solicitar medidas del muro
alto = float(input("Ingrese el alto del muro en metros: "))
ancho = float(input("Ingrese el ancho del muro en metros: "))

# Calcular el área del muro
area = alto * ancho

# Calcular número de cajas necesarias
caja_metros = 3.5
cajas_necesarias = area / caja_metros

# Redondear hacia arriba porque no se puede comprar media caja
import math
cajas_redondeadas = math.ceil(cajas_necesarias)

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Área del muro: {area:.2f} m²")
print(f"Cajas necesarias (sin redondear): {cajas_necesarias:.2f}")
print(f"Cajas que debe comprar: {cajas_redondeadas}")

"""Un atleta tiene la costumbre de medir el tiempo (en minutos) y la distancia (en metros)
durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
tiempo que duro el entrenamiento, la distancia recorrida, y el promedio del tiempo y la
distancia recorrida."""

# Día 1
tiempo1 = float(input("Tiempo del día 1 (minutos): "))
distancia1 = float(input("Distancia del día 1 (metros): "))

# Día 2
tiempo2 = float(input("\nTiempo del día 2 (minutos): "))
distancia2 = float(input("Distancia del día 2 (metros): "))

# Día 3
tiempo3 = float(input("\nTiempo del día 3 (minutos): "))
distancia3 = float(input("Distancia del día 3 (metros): "))

# Totales
tiempo_total = tiempo1 + tiempo2 + tiempo3
distancia_total = distancia1 + distancia2 + distancia3

# Promedios
tiempo_promedio = tiempo_total / 3
distancia_promedio = distancia_total / 3

# Resultados
print("\n--- Resultados del entrenamiento ---")
print(f"Tiempo total: {tiempo_total:.2f} minutos")
print(f"Distancia total: {distancia_total:.2f} metros")
print(f"Promedio de tiempo: {tiempo_promedio:.2f} minutos")
print(f"Promedio de distancia: {distancia_promedio:.2f} metros")


"""Una madre y sus 4 hijos se acercan a recibir información por parte de un abogado
referente al dinero que les corresponde en una herencia dejada por su esposo y padre
respectivamente."""

# Solicitar el valor total de la herencia
herencia_total = float(input("Ingrese el valor total de la herencia: "))

# Número de beneficiarios
beneficiarios = 5  # 1 madre + 4 hijos

# Calcular la parte que le corresponde a cada uno
parte_individual = herencia_total / beneficiarios

# Mostrar resultados
print("\n--- Distribución de la herencia ---")
print(f"Herencia total: ${herencia_total:.2f}")
print(f"Cada beneficiario recibe: ${parte_individual:.2f}")


"""El testamento tiene las siguientes condiciones: A la esposa le corresponde el 40% mientras
que a los hijos les corresponde: 30% 20% 40% 10% respectivamente. Se pide un algoritmo
que lea los datos necesarios, y muestre lo que le corresponde a la esposa y a los hijos."""

# Solicitar el valor total de la herencia
herencia_total = float(input("Ingrese el valor total de la herencia: "))

# Porcentajes
porcentaje_esposa = 0.40
porcentajes_hijos = [0.30, 0.20, 0.40, 0.10]

# Cálculos
parte_esposa = herencia_total * porcentaje_esposa
parte_hijos = [herencia_total * p for p in porcentajes_hijos]

# Mostrar resultados
print("\n--- Distribución de la herencia ---")
print(f"Herencia total: ${herencia_total:.2f}")
print(f"Esposa recibe (40%): ${parte_esposa:.2f}")

for i, parte in enumerate(parte_hijos, start=1):
    print(f"Hijo {i} recibe ({int(porcentajes_hijos[i-1]*100)}%): ${parte:.2f}")


"""El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
metros cuadrados e imprimir el área para cada destino, y el área que queda disponible
para otros proyectos."""

# Leer el área total del terreno
area_total = float(input("Ingrese el área total del terreno en metros cuadrados: "))

# Porcentajes de uso
cultivos = area_total * 0.40
vivienda = area_total * 0.25
zonas_verdes = area_total * 0.15

# Área restante
area_disponible = area_total - (cultivos + vivienda + zonas_verdes)

# Mostrar resultados
print("\n--- Distribución del terreno ---")
print(f"Área total: {area_total:.2f} m²")
print(f"Área para cultivos (40%): {cultivos:.2f} m²")
print(f"Área para vivienda (25%): {vivienda:.2f} m²")
print(f"Área para zonas verdes (15%): {zonas_verdes:.2f} m²")
print(f"Área disponible para otros proyectos: {area_disponible:.2f} m²")


"""En clase de programación, se sacan 4 notas del 15%,30%,30%,25% respectivamente. Se
pide diseñar un algoritmo que permita mostrar la nota definitiva de un estudiante.
Teniendo en cuenta que la primera nota consta del promedio de dos talleres, la segunda
de tres evaluaciones, la tercera nota de un trabajo final y la última es el promedio de 4
quizzes."""

# Ingreso de notas
print("Ingrese las notas de los dos talleres:")
taller1 = float(input("Taller 1: "))
taller2 = float(input("Taller 2: "))
nota1 = (taller1 + taller2) / 2

print("\nIngrese las notas de las tres evaluaciones:")
eval1 = float(input("Evaluación 1: "))
eval2 = float(input("Evaluación 2: "))
eval3 = float(input("Evaluación 3: "))
nota2 = (eval1 + eval2 + eval3) / 3

print("\nIngrese la nota del trabajo final:")
nota3 = float(input("Trabajo final: "))

print("\nIngrese las notas de los cuatro quizzes:")
quiz1 = float(input("Quiz 1: "))
quiz2 = float(input("Quiz 2: "))
quiz3 = float(input("Quiz 3: "))
quiz4 = float(input("Quiz 4: "))
nota4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4

# Cálculo de nota definitiva
nota_definitiva = (nota1 * 0.15) + (nota2 * 0.30) + (nota3 * 0.30) + (nota4 * 0.25)

# Mostrar resultados
print("\n--- Resultado Final ---")
print(f"Nota definitiva del estudiante: {nota_definitiva:.2f}")


"""El sistema de liquidación que hacen los conductores de buses y los colectivos a las
diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro
al terminarlo. La diferencia de estos dos números determina el número de pasajeros
transportados en el día. Realizar un algoritmo que permita leer estos dos números y el
valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y
el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes
del dinero mientras el conductor recibe el resto."""

# Leer datos de la registradora
inicio = int(input("Número inicial de la registradora: "))
fin = int(input("Número final de la registradora: "))

# Leer valor del pasaje
valor_pasaje = float(input("Valor del pasaje: "))

# Calcular número de pasajeros
pasajeros = fin - inicio

# Calcular total recaudado
total_recaudado = pasajeros * valor_pasaje

# Distribución del dinero
empresa = total_recaudado * 0.75
conductor = total_recaudado * 0.25

# Mostrar resultados
print("\n--- Liquidación del día ---")
print(f"Pasajeros transportados: {pasajeros}")
print(f"Total recaudado: ${total_recaudado:.2f}")
print(f"Liquidado a la empresa (75%): ${empresa:.2f}")
print(f"Liquidado al conductor (25%): ${conductor:.2f}")





