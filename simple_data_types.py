# print("¡Hola Mundo!")


# variable = "¡Hola Mundo!"
# print(variable)


# nombre = input("¿Cual es tu nombre?: ")
# print("¡Hola " + nombre + "!")


# print(((3 + 2) / (2 * 5)) ** 2) 


# horas = float(input("¿Cuantas horas por dia trabajas?: "))
# coste = float(input("¿Cuanto cobras por hora?: "))
# paga = horas * coste
# print("Te corresponden", paga, "por dia")


# n = int(input("Introduce un número entero: "))
# suma = n * (n + 1) / 2
# print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))


# peso = input("¿Cual es tu peso en kg? ") # responder con decimales, 62.5
# estatura = input("¿Cual es tu estatura en metros? ")
# imc = round(float(peso) / float(estatura)**2,2)
# print("Tu índice de masa corporal es " + str(imc))


# n = input("Introduce el dividendo (entero): ")
# m = input("Introduce el divisor (entero): ")
# print(n + " entre " + m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))


# cantidad = float(input("Cuanto dinero invertirá?: "))
# interes = float(input("Interes porcentual anual?: "))
# anos = int(input("Años?: "))
# print("Capital obtenido final: " + str(round(cantidad * (interes / 100 + 1) ** anos, 2)))


# peso_payaso  = 112 
# peso_muneca = 75 
# payasos = int(input("Introduce el número de payasos a enviar: "))
# munecas = int(input("Introduce el número de muñecas a enviar: "))
# peso_total = peso_payaso * payasos + peso_muneca * munecas
# print("El peso total del paquete es " + str(peso_total))


# inversion = float(input("Introduce la inversion inicial: "))
# interes = 0.04
# balance1 = inversion * (1 + interes)
# print("Balance tras el primer año:" + str(round(balance1, 2)))
# balance2 = balance1 * (1 + interes)
# print("Balance tras el segundo año:" + str(round(balance2, 2)))
# balance3 = balance2 * (1 + interes)
# print("Balance tras el tercer año:" + str(round(balance3, 2)))


# barra_pan = int(input("Introduce el numero de barras vendidas que no son frescas: "))
# precio = 3.49
# descuento = 0.6
# coste = barra_pan * precio * (1 - descuento)
# print("El coste de una bara fresca es " + str(precio) + " €")
# print("El descuento sobre una barra no fresca es " + str(descuento * 100) + " %")
# print("El coste final a pagar es " + str(round(coste, 2)) + " €")