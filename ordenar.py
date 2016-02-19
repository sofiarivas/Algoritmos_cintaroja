numeros = [10,5,9,1]

numeros_ordenados = [ ]

for elem in numeros:
	numero_anterior = elem
	if elem <= 0:
		numeros_ordenados.insert(0,0)
	elif elem >= numero_anterior:
		numeros_ordenados.append(elem)
	#elif elem <= numero_anterior:
	print(numeros_ordenados)

