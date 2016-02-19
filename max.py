numeros = [10,5,9,1,3,4,6,3,2,3]
numeros_ordenados = []

while len(numeros)>0:
	max = numeros[0]

	for elem in numeros[1:]:
		if elem > max :
			max = elem

	numeros_ordenados.append(max)
	numeros.remove(max)

print(numeros_ordenados)sub
