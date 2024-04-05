from zeep import Client

# Crear un cliente para el servicio web
client = Client("http://localhost:8000/")

# Llamar al método sumar_numeros del servicio web
resultado = client.service.SumaDosNumeros(x=1, y=1)
# Imprimir el resultado
print(resultado)

# Llamar al método sumar_numeros del servicio web
resultado = client.service.RestaDosNumeros(x=1, y=1)
# Imprimir el resultado
print(resultado)

# Llamar al método sumar_numeros del servicio web
resultado = client.service.MultiplicaDosNumeros(x=1, y=1)
# Imprimir el resultado
print(resultado)

# Llamar al método sumar_numeros del servicio web
resultado = client.service.DivideDosNumeros(x=1, y=0)
# Imprimir el resultado
print(resultado)