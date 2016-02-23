lista_letras = list(input("Dame una lista de letras="))
print(lista_letras)
consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vocales = ["A", "E", "I", "O","U"]
contador_vocales = 0
contador_consonates = 0

for elem in lista_letras:
	elem = elem.upper()
	if (elem == "A") or (elem == "E") or (elem == "I") or (elem == "O") or (elem == "U"):
		
		contador_vocales = contador_vocales + 1
	else:			
		contador_consonates = contador_consonates + 1

print("Tienes",contador_consonates,"consonantes,", "y tienes", contador_vocales, "vocales.")