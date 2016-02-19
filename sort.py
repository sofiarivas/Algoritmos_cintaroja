numeros = [10,5,9,1,3,4,6,3,2,3]
numeros_ordenados = []

while len(numeros)>0:
	minimo = numeros[0]

	for elem in numeros[1:]:
		if elem < minimo :
			minimo = elem

	numeros_ordenados.append(minimo)
	numeros.remove(minimo)

print(numeros_ordenados)






