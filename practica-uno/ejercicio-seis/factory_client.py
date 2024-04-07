import requests
import json

# Definimos la URL del servicio al que vamos a hacer las peticiones
url = "http://localhost:8000/animales"

# Definimos los encabezados HTTP que vamos a enviar con las peticiones
headers = {"Content-Type": "application/json"}

# Datos para la petición POST (Añadir un nuevo animal)
new_animal_data = {
    "animal_type": "mamifero",
    "name": "Elefante",
    "species": "Loxodonta africana",
    "gender": "Male",
    "age": 15,
    "weight": 5000
}

# Petición POST para añadir un nuevo animal
response = requests.post(url=url, json=new_animal_data, headers=headers)
print("Respuesta POST:", response.json())

# Datos para la petición PUT (Actualizar un animal existente)
update_animal_data = {
    "name": "Elefante Gigante",
    "weight": 6000
}

# Petición PUT para actualizar un animal existente (se asume que el animal con ID 1 ya existe)
update_response = requests.put(f"{url}/0", json=update_animal_data, headers=headers)
print("Respuesta PUT:", update_response.json())

# Petición GET para obtener todos los animales
get_response = requests.get(url)
print("Respuesta GET:", get_response.json())

# Petición DELETE para eliminar un animal (se asume que el animal con ID 1 existe)
delete_response = requests.delete(f"{url}/0")
print("Respuesta DELETE:", delete_response.json())
