from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation, Float,Boolean

class Planta(ObjectType):
    ID = Int()
    nombre = String()
    especie = String()
    edad = Int()
    altura = Float()
    frutos = Boolean()

class Query(ObjectType):
    plantas = List(Planta)
    plantas_por_especie = List(Planta, especie=String())
    plantas_por_frutos = List(Planta)
    

    def resolve_plantas(root, info):
        return plantas


    def resolve_plantas_por_especie(info, root, especie):
        PE = []
        for planta in plantas: 
            if planta.especie == especie:PE.append(planta)
        return PE

    def resolve_plantas_por_frutos(info, root):
        PF = []
        for planta in plantas:
            if planta.frutos:
                PF.append(planta)
        return PF    
        
class CrearPlanta(Mutation):
    class Arguments:
        nombre = String()
        especie = String()
        edad = Int()
        altura = Float()
        frutos = Boolean()
    planta = Field(Planta)
    
    def mutate(root, info,  nombre, especie, edad, altura, frutos):
        
        nueva_planta = Planta(
            ID = len(plantas)+1,
            nombre = nombre,
            especie = especie,
            edad = edad,
            altura = altura,
            frutos = frutos
        )
        plantas.append(nueva_planta)
        return CrearPlanta(planta = nueva_planta)

class EliminarPlanta(Mutation):
    class Arguments:
        id = Int()
    planta = Field(Planta)
    
    def mutate(root, info,  id):
        for i, planta in enumerate(plantas):
            if planta.ID == id:
                plantas.pop(i)
                return EliminarPlanta(planta = planta)
        return "lo sentimos"
    
class ModificarPlanta(Mutation):
    class Arguments:
        id  = Int()
        nombre = String()
        especie = String()
        edad = Int()
        altura = Float()
        frutos = Boolean()
    planta = Field(Planta)
    def mutate(root, info, id, nombre, especie, edad, altura, frutos):
        for planta in plantas:
            if planta.ID == id:
                planta.nombre = nombre,
                planta.especie = especie
                planta.edad = edad,
                planta.altura = altura,
                planta.frutos = frutos
        return ModificarPlanta(planta = planta)
        

class Mutations(ObjectType):
    crear_planta = CrearPlanta.Field(),
    eliminar_planta = EliminarPlanta.Field(),
    modificar_planta = ModificarPlanta.Field()
plantas = [
    Planta(ID=1, nombre='Rosa', especie='Rosa indica', edad=2, altura=0.3, frutos=False),
    Planta(ID=2, nombre='Girasol', especie='Helianthus annuus', edad=1, altura=0.6, frutos=False),
    Planta(ID=3, nombre='Orquídea', especie='Phalaenopsis', edad=4, altura=0.5, frutos=False),
    Planta(ID=4, nombre='Lirio', especie='Lilium', edad=3, altura=0.4, frutos=True)
]  
schema = Schema(query=Query, mutation=Mutations)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            print(data)
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()