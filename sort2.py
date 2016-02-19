numeros = [10,5,9,1]
minimo = numeros[0]
numeros_ordenados = [ ]

for elem in numeros[1:]:
	if elem < minimo :
		minimo = elem
	elif elem > minimo:
		numeros_ordenados.append(elem)




