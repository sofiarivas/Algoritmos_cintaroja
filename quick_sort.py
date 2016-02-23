# -*- coding: utf8 -*-

lista_num = [0,2,1,7,0,8,5,78,9,12,33]

def quick_sort(lista_num):

	minimos = []
	maximos = []
	iguales_pivots = []

	#Limite para la recusión, cuando una lista este vacia.
	if len(lista_num) == 0:
		return lista_num

	#Selecciono un pivot, el primer elemento de la lista.
	pivot = lista_num[0]

	#Por cada elemento de mi lista original, voy a hacer una comparación
	for num in lista_num:

		#Si el numero es menor que el pivot, va a la lista de menores
		if num < pivot:
			minimos.append(num)
	
		#Si el numero es igual al pivot va a la lista de iguales / pivtos
		elif num == pivot:
			iguales_pivots.append(num)

		#Si el numero es mayor al pivot va a la lista de maximos
		else:
			maximos.append(num)

	#En el return se encuentra la recursión, el mismo proceso se corre sobre la lista de minimos o maximos hasta que queden vacias.
	return quick_sort(minimos) + iguales_pivots + quick_sort(maximos)

print(quick_sort(lista_num))

	
