from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

messages = []


class MessageService:
    @staticmethod
    def find_message(id):
        return next(
            (message for message in messages if message["id"] == id),
            None,
        )
    @staticmethod
    def encrypt_message(message):
        message_encrypted=""
        vec=['x','y','z']
        for letter in message:
            if letter in vec: message_encrypted += chr(ord('a')+vec.index(letter))
            else: message_encrypted += chr(ord(letter)+3)
        return message_encrypted    
            
    @staticmethod
    def add_message(data):
        if not messages: data["id"] = 1
        else: data["id"] = max(messages, key=lambda x: x["id"])["id"]+1
        
        data["content_encrypted"]= MessageService.encrypt_message(data["content"])
        messages.append(data)
        return messages

    @staticmethod
    def update_message(id, data):
        message = MessageService.find_message(id)
        data["content_encrypted"] = MessageService.encrypt_message(data["content"])
        if message:
            messages.update(data)
            return messages
        else:
            return None

    @staticmethod
    def delete_messages_by_id(id):
        message = MessageService.find_message(id)
        if message: 
            messages.remove(message)
            return message
        else: return None
        

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if self.path == "/messages":
            HTTPResponseHandler.handle_response(self,200, messages)
        elif self.path.startswith("/messages/"):
            id = int(self.path.split("/")[-1])
            message = MessageService.find_message(id)
            if message:
                HTTPResponseHandler.handle_response(self, 200, [message])
            else:
                HTTPResponseHandler.handle_response(self, 204, [])
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )


    def do_POST(self):
        if self.path == "/messages":
            data = self.read_data()
            messages = MessageService.add_message(data)
            HTTPResponseHandler.handle_response(self, 201, messages)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_PUT(self):
        if self.path.startswith("/messages/"):
            id = int(self.path.split("/")[-1])
            data = self.read_data()
            messages = MessageService.update_message(id, data)
            if messages:
                HTTPResponseHandler.handle_response(self, 200, messages)
            else:
                HTTPResponseHandler.handle_response(
                    self, 404, {"Error": "mensaje no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_DELETE(self):
        if self.path.startswith("/messages/"):
            id = int(self.path.split("/")[-1])
            message = MessageService.delete_messages_by_id(id)
            if message:
                HTTPResponseHandler.handle_response(self, 200, message)
            else:
                HTTPResponseHandler.handle_response(self, 404, "Message not found")
                
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()