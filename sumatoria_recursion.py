def suma(lista):
	if lista:
		return lista[0] + suma(lista[1:])
	else:
		return 0

print(suma([1,2,3,4]))