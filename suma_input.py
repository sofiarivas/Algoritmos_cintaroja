# lista = input("Dame una lista de numeros").split(" ")
lista = list(map(int,input("Dame una lista de números=").split(" ")))
print(lista)
# lista_n = []



# for l in lista:
# 	l = int(l)
# 	lista_n.append(l)

total_suma = 0

for num in lista:
	total_suma+=num
print(total_suma)