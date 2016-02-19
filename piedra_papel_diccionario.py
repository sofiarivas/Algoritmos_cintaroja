import random
#Piedra papel o Python
opciones=["PIEDRA", "PAPEL","TIJERAS"]
reglas = {
	"piedra": {"papel": "El papel cubre a la piedra, pierdes.",
				"tijeras": "La piedra rompe las tijeras, ganas."},
	"papel": {"piedra": "El papel le gana a la piedra, GANASTE!",
				"tijeras": "Las tijeras le ganan al papel, pierdes."},
	"tijeras": {"piedra": "Las tijeras pierden contra la piedra, perdiste",
				"papel": "Las tijeras le ganan al papel, ganas."}
}
print("Listo para jugar!\n")
usuario_arma = input("¿Qué quieres escoger (Piedra, Papel o tijeras)").lower()
print("Tu eliges: ",usuario_arma)
usuario_arma = usuario_arma
computadora_arma= opciones[random.randint(0,2)]
computadora_arma = computadora_arma.lower()
print("La computadora elige: ",computadora_arma)
if usuario_arma == computadora_arma:
	print("Empateeeee")
else:
	print(reglas[usuario_arma][computadora_arma])