# -*- coding: utf8 -*-

#Recibo una lista de números.
lista_num = [2,1,7,0,8,5]

#Listas donde se agregan los numeros mayores, menores e iguales.
minimos = []
maximos = []
iguales_pivots = []



def quick_sort(lista_num):

	if len(lista_num) == 0:
		return lista_num
	#Selecciono un pivot
	pivot = lista_num[0]
	lista_num.remove(pivot)
	iguales_pivots.append(pivot)

	for num in lista_num:
		print(num)
		if num < pivot:
			minimos.append(num)
			lista_num.remove(num)
		elif num == pivot:
			iguales_pivots.append(num)
			lista_num.remove(num)
		else:
			maximos.append(num)
			lista_num.remove(num)
	print ("estos son minimos", minimos, "estos son pivots", iguales_pivots, "Estos son maximos", maximos)
	return quick_sort(minimos) + iguales_pivots + quick_sort(maximos)



print(quick_sort(lista_num))

	
