import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# query_lista = """
# {
#         plantas{
#             ID
#             nombre
#             especie
#             edad
#             altura
#             frutos
#         }
# }
# """
# print("\n- Buscar plantas por especie\n")
# # Lista de todas las plantas
# response = requests.post(url, json={'query': query_lista})
# print(response.text)

# query_lista_especie = """
# {
#         plantasPorEspecie(especie:"Rosa indica"){
#             ID
#             nombre
#         }
# }
# """
# print("\n- Buscar plantas por especie\n")
# response = requests.post(url, json={'query': query_lista_especie})
# print(response.text)

# query_frutos= """
# {
#     plantasPorFrutos{
#         nombre
#     }
# }
# """
# print("\n- Buscar plantas por especie\n")
# response = requests.post(url, json={'query': query_frutos})
# print(response.text)

query_eliminar = """
mutation 
{
    eliminarPlanta(id: 1) {
        planta(){
        }
    }
}
"""


print("\n Elimina un estudiante\n")
response = requests.post(url, json={'query': query_eliminar})
print(response.text)

# print("\n Elimina un estudiante\n")
# response = requests.post(url, json={'query': query_lista})
# print(response.text)
query_crear_planta = """
mutation {
    crearPlanta(nombre: "A", especie: "E", edad: 5, altura:1.3, frutos: True){
        planta {
            ID
            nombre
            especie
            edad
            altura
            frutos
        }
    }
}
"""

# Enviar la consulta al servidor GraphQL
response = requests.post(url, json={'query': query_crear_planta})
print(response.text)