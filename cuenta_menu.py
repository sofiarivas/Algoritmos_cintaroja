# -*- coding: utf8 -*-

menu={"burrito": "Machaca"}
menu["taco"] = "Pastor"
menu["torta"] = "Milanesa"
pedido = []

print("Bienvenido este es nuestro menu: ")

for key,val in menu.items():
	#Construir una cadena de text que incluya variables.
	print("Tenemos {} de {} ".format(key,val))

# CMD + shift + 7 para comentar y descomentar

orden = input("Que se te antoja?").lower()

while orden.upper() != "Q":

		if menu.get(orden):
			pedido.append(orden)
			#sep sirve para agregar algo como separación en donde yo ponga comas.
			print("Tu pedido fue:",pedido, sep = " - ")
			orden = input("Que se te antoja? (si terminaste presionas Q)").lower()
		else:
			print("Esto no es esta disponible en nuestro menu")
			orden = input("Agrega otra opción? (si terminaste presionas Q)").lower()

print("Tu pedido es:")
for num in range(len(pedido)):
	print(num+1,pedido[num], sep=".-")

