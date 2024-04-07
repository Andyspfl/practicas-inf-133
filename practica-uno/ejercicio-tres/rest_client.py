import requests

url = "http://localhost:8000/"

# Crear un paciente
nuevo_paciente_1 = {
    "nombre": "Carlos",
    "apellido": "Lopez",
    "edad": 45,
    "genero": "Masculino",
    "diagnostico": "Diabetes",
    "doctor": "Dra. Martinez"
}
ruta_post_paciente_1 = url + "patients"
post_response_paciente_1 = requests.post(ruta_post_paciente_1, json=nuevo_paciente_1)
print("\nCrear un paciente:\n")
print(post_response_paciente_1.text)

nuevo_paciente_2 = {
    "CI": 2,
    "nombre": "Ana",
    "apellido": "Garcia",
    "edad": 35,
    "genero": "Femenino",
    "diagnostico": "Hipertension",
    "doctor": "Dr. Rodriguez"
}
ruta_post_paciente_2 = url + "patients"
post_response_paciente_2 = requests.post(ruta_post_paciente_2, json=nuevo_paciente_2)
print("\nCrear un paciente:\n")
print(post_response_paciente_2.text)

nuevo_paciente_3 = {
    "CI": 3,
    "nombre": "Luis",
    "apellido": "Martinez",
    "edad": 50,
    "genero": "Masculino",
    "diagnostico": "Diabetes",
    "doctor": "Dra. Martinez"
}
ruta_post_paciente_3 = url + "patients"
post_response_paciente_3 = requests.post(ruta_post_paciente_3, json=nuevo_paciente_3)
print("\nCrear un paciente:\n")
print(post_response_paciente_3.text)

# Listar todos los pacientes
ruta_get_pacientes = url + "patients"
get_response_pacientes = requests.get(ruta_get_pacientes)
print("\nListar todos los pacientes:\n")
print(get_response_pacientes.text)

# Buscar pacientes por CI
ruta_get_paciente_id_2 = url + "patients/2"
get_response_paciente_id_2 = requests.get(ruta_get_paciente_id_2)
print("\nBuscar pacientes por CI:\n")
print(get_response_paciente_id_2.text)

# Listar a los pacientes que tienen diagnostico de `Diabetes`
ruta_get_pacientes_diabetes = url + "patients?diagnostico=Diabetes"
get_response_pacientes_diabetes = requests.get(ruta_get_pacientes_diabetes)
print("\nListar a los pacientes que tienen diagnostico de `Diabetes`:\n")
print(get_response_pacientes_diabetes.text)

# Listar a los pacientes que atiende el Doctor `Dra. Martinez`
ruta_get_pacientes_doctor = url + "patients?doctor=Dra. Martinez"
get_response_pacientes_doctor = requests.get(ruta_get_pacientes_doctor)
print("\nListar a los pacientes que atiende el Doctor `Dra. Martinez`:\n")
print(get_response_pacientes_doctor.text)

# Actualizar la informacion de un paciente
ruta_put_paciente_1 = url + "patients/1"
nuevos_datos_paciente_1 = {
    "nombre": "Nuevo nombre",
    "edad": 40
}
put_response_paciente_1 = requests.put(ruta_put_paciente_1, json=nuevos_datos_paciente_1)
print("\nActualizar la informacion de un paciente:\n")
print(put_response_paciente_1.text)

# Eliminar un paciente
ruta_delete_paciente_3 = url + "patients/3"
delete_response_paciente_3 = requests.delete(ruta_delete_paciente_3)
print("\nEliminar un paciente:\n")
print(delete_response_paciente_3.text)
