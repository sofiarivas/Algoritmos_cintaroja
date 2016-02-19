#necesito tener un entorno virtual
#python3 -m venv .-- linea de comando para crear un entorno virtual.

#activo mi entorno
#source miEntorno/bin/activate 

import requests
#importo mi Json

#LLAMANDO UN JSON

# my_request=requests.get('http://fixter.org/devf/batch8.json')
# lista=my_request.json()
# print(lista)

#LLAMANDO UNA API REAL

my_request=requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=44db6a862fba0b067b1930da0d769e98')
lista=my_request.json()

elMain = lista['main']
temperatura = int(elMain['temp'])



print(temperatura)