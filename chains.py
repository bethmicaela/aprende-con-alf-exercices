# nombre = input("Cual es tu nombre?: ")
# n = input("Elige un numero entero: ")
# print((nombre + "\n")  * int(n))

# nombre = input("Introduce tu nombre completo: ")
# print(nombre.lower() + "\n" + nombre.upper() + "\n" + nombre.title()) # lower:  minuscula, upper: mayuscula, title: mayus la primer letra de c/palabra

# nombre = input("Introduce tu nombre: ")
# print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")  # len:  cuenta las letras

# telefono = input("Introduce tu numero telefonico con el formato +xx-xxxxxxxxx-xx: ")
# print("El numero telefonico es ", telefono[4:-3])  # imprime los numeros de 4 a -3 (slices)

# frase = input("Introduce un frase: ")
# print(frase[::-1]) # imprime la frase invertida

# frase = input("Introduce una frase: ")
# vocal = input("Introduce una vocal en minuscula: ")
# print(frase.replace(vocal, vocal.upper())) #  remplaza en mayuscula la vocal de la frase

# email = input("Introduce tu correo electronico: ")
# print(email[:email.find("@")] + "@ceu.es") # imprimir el email, hasta encontrar el @ y "remplazarlo" por @ceu.es

# precio = input("introduce el precio del producto con dos decimales: ")
# print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:], "centécimos.")  # imprimir precio hasta encontrar un punto, "euros de", imprimir lo que le sigue al punto sin incluirlo(por eso sumo +1, "centesimos")

# fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
# dia = fecha[:fecha.find("/")] # fecha hasta encontra una barra
# mesano = fecha[fecha.find("/")+1:] # sirve para ejecutar lo demás
# mes = mesano[:mesano.find("/")] # mesano(despues de la primer barra) hasta encontrar otra barra
# ano = mesano[mesano.find("/")+1:] # mesano despues de la segunda barra
# print("Dia", dia + "\n" "Mes", mes + "\n" "Año", ano)

# cesta = input("Introduzca los productos de la cesta de compra separados por comas: ")
# print(cesta.replace(", ", "\n")) # en cada coma saltar una linea

# producto = input("Introduzca nombre del producto a comprar: ")
# precio = float(input("Introduzca el precio con sus decimales: "))
# unidades = int(input("Introduzca número de unidades que desea: "))
# precio_total = precio * unidades
# precio_unitario = round(precio_total, 2)
# # print("El producto", producto, ":  tiene" ,unidades, "unidades x",  )  
# print(f'El producto {producto} cuesta ${precio} x las unidades {unidades} da un total de {precio_total}')  