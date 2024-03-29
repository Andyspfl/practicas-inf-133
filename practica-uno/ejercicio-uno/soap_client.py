from zeep import Client

# Crear un cliente para el servicio web
client = Client("http://localhost:8000/")

# Llamar al método sumar_numeros del servicio web
resultado = client.service.SumaDosNumeros(num1=1, num2=1)
# Imprimir el resultado
print(resultado)

# Llamar al método sumar_numeros del servicio web
resultado = client.service.RestaDosNumeros(num1=1, num2=1)
# Imprimir el resultado
print(resultado)

# Llamar al método sumar_numeros del servicio web
resultado = client.service.MultiplicaDosNumeros(num1=1, num2=1)
# Imprimir el resultado
print(resultado)

# Llamar al método sumar_numeros del servicio web
resultado = client.service.DivideDosNumeros(num1=1, num2=0)
# Imprimir el resultado
print(resultado)