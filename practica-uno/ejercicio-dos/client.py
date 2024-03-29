import requests

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'


print("\nCrear una nueva planta\n")
query_crear_planta = """
mutation {
    crearPlanta(nombre: "A", especie: "E", edad: 5, altura:1.3, frutos: true){
        planta {
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
}
"""

response_mutation = requests.post(url, json={'query': query_crear_planta})
print(response_mutation.text)

print("\n- Listar todas las plantas\n")
query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
}
"""
# Lista de todas las plantas
response = requests.post(url, json={'query': query_lista})
print(response.text)

print("\n- Buscar plantas por especie\n")
query_lista_especie = """
{
        plantasPorEspecie(especie:"Rosa indica"){
            id
            nombre
        }
}
"""
response = requests.post(url, json={'query': query_lista_especie})
print(response.text)

print("\n- Buscar las plantas que tienen frutos\n")
query_frutos= """
{
    plantasPorFrutos{
        nombre
    }
}
"""
response = requests.post(url, json={'query': query_frutos})
print(response.text)

print("\n- Actualizar la información de una planta\n")
query_modificar_planta = """
mutation {
    modificarPlanta(id: 1, nombre: "Nuevo nombre", especie: "Nueva especie", edad: 10, altura: 2.5, frutos: true) {
        planta {
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
}
"""
# Enviar la solicitud POST al servidor GraphQL
responses = requests.post(url, json={'query': query_modificar_planta})
print(responses.text)

query_eliminar = """
mutation {
        eliminarPlanta(id: 3) {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""

print("\n- Eliminar una planta\n")
response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)


print("\n- Listar todas las plantas\n")
response = requests.post(url, json={'query': query_lista})
print(response.text)