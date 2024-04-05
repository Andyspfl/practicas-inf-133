import requests

url = "http://localhost:8000/messages"

# Crear un mensaje
print("Crear un mensaje:")
new_message_1 = {
    "content": "Juanito"
}
post_response_1 = requests.request(method="POST", url=url, json=new_message_1)

new_message_2 = {
    "content": "Maria"
}
post_response_2 = requests.request(method="POST", url=url, json=new_message_2)

new_message_3 = {
    "content": "Pedro"
}
post_response_3 = requests.request(method="POST", url=url, json=new_message_3)
print(post_response_3.text)

# Listar todos los mensajes
print("\nListar todos los mensajes:")
get_response = requests.request(method="GET", url=url)
print(get_response.text)

# Buscar mensajes por ID
print("\nBuscar mensajes por ID:")
get_by_id_url = f"{url}/1"  # Reemplaza 1 con el ID del mensaje que deseas buscar
get_by_id_response = requests.request(method="GET", url=get_by_id_url)
print(get_by_id_response.text)

# Actualizar el contenido de un mensaje
print("\nActualizar el contenido de un mensaje:")
update_url = f"{url}/4"  # Reemplaza 1 con el ID del mensaje que deseas actualizar
message_update = {
    "content": "Juancin"
}
put_response = requests.request(method="PUT", url=update_url, json=message_update)
print(put_response.text)

# Eliminar un mensaje
print("\nEliminar un mensaje:")
delete_url = f"{url}/2"  # Reemplaza 1 con el ID del mensaje que deseas eliminar
delete_response = requests.request(method="DELETE", url=delete_url)
print(delete_response.text)

# Listar todos los mensajes
print("\nListar todos los mensajes:")
get_response = requests.request(method="GET", url=url)
print(get_response.text)

