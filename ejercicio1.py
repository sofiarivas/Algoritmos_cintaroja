
# -*- coding: utf8 -*-

# COMENTARIOS
# Sumar una colección de números de tres formas diferentes

x = int(input("Cuantos numeros vas a sumar:"))

def primeraSuma(x):
    numero = 0
    for y in range(x):
        numero2 = int(input("Inserta numero para sumar:"))
        numero = numero + numero2

    print(numero)
    pass
    
primeraSuma(x)

#range(19)
#range (5,20)
#range(5,20,5)

