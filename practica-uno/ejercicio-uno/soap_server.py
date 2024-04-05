from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

sumar_numeros = lambda x,y: x+y
restar_numeros = lambda x,y: x-y
multiplicar_numeros = lambda x,y: x*y
dividir_numeros = lambda x,y: "Cannot divide by zero" if y==0 else x/y

dispatcher = SoapDispatcher(
    "Dispatcher-practica",
    location="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "SumaDosNumeros",
    sumar_numeros,
    returns={"suma": str},
    args={"x": int, "y": int},
)

dispatcher.register_function(
    "RestaDosNumeros",
    restar_numeros,
    returns = {"resta": str},
    args = {"x": int, "y": int}
)
dispatcher.register_function(
    "MultiplicaDosNumeros",
    multiplicar_numeros,
    returns = {"multiplicacion": str},
    args ={"x": int, "y": int}
)
dispatcher.register_function(
    "DivideDosNumeros",
    dividir_numeros,
    returns = {"divicion": str},
    args ={"x": int, "y": int}
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()