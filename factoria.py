# Factorial

def factorial(n):

	if n == 0:
		return 1

	
	return n * factorial(n-1)

pass

print(factorial(4))

#Iteracion

def factorial(n):
	multiplicador = 1

	if n == 0 :
		return 1
	
	elif n > 0:

		for elem in range(1,n+1):
			
			multiplicador = multiplicador * elem

		return multiplicador

print(factorial(4))

