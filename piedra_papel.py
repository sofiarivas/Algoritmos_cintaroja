# -*- coding: utf8 -*-
import random
#Piedra papel o Python
opciones=["PIEDRA", "PAPEL","PYTHON"]
reglas = {
	"piedra": {"papel": "El papel cubre a la piedra, pierdes.",
				"tijeras": "La piedra rompe las tijeras, pierdes."}
}
print("Listo para jugar!\n")
usuario_arma = input("¿Qué quieres escoger (Piedra, Papel o Python)").lower()
print("Tu eliges: ",usuario_arma)
usuario_arma = usuario_arma.upper()
computadora_arma= opciones[random.randint(0,2)]

print("La computadora elige: ",computadora_arma)


if usuario_arma == computadora_arma:
	print("Empateeeee")

if usuario_arma == "PIEDRA":
	if computadora_arma == "PAPEL":
		print("Perdiste")
	elif computadora_arma == "PYTHON":
		print("Ganaste")

if usuario_arma == "PAPEL":
	if computadora_arma == "PIEDRA":
		print("GANASTE")
	elif computadora_arma == "PYTHON":
		print("PERDISTE")

if usuario_arma == "PYTHON":
	if computadora_arma == "PIEDRA":
		print("PIERDES")
	elif computadora_arma == "PAPEL":
		print("GANASTE")



# if usuario_arma == "piedra" or usuario_arma == "PIEDRA":
# 	if computadora_arma == "PIEDRA":
# 		print("Esto es un empate")