lista_letras = list(input("Dame una lista de letras="))
print(lista_letras)
consonantes = ["B", "C", "D", "F", "G"]
vocales = ["A", "E", "I", "O","U"]
lista_vocales = []
lista_consontantes = []
contador_vocales = 0
contador_consonates = 0

# def vocales_consonantes(lista_letras):
for elem in lista_letras:
	elem = elem.upper()
	if (elem == "A") or (elem == "E") or (elem == "I") or (elem == "O") or (elem == "U"):
		lista_vocales.append(elem)
		contador_vocales = len(lista_vocales)
	else:			
		lista_consontantes.append(elem)
		contador_consonates = len(lista_consontantes)

print("Tienes tantas consonantes:",contador_consonates,"Tienes tantas vocales:", contador_vocales)


