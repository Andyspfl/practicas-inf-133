from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

patients = []


class PatientsService:
    @staticmethod
    def find_patients(CI):
        return next(
            (patient for patient in patients if patient["CI"] == CI),
            None,
        )
    @staticmethod
    def find_patient_by_doctor(name):
        doctors = [patient for patient in patients if patient["doctor"] == name]
        return doctors
        
    @staticmethod
    def find_patient_by_diagnostic(name):
        diagnostics = [patient for patient in patients if patient["diagnostico"] == name]
        return diagnostics
    
    @staticmethod
    def add_patient(data):
        if not patients: data["CI"] = 1
        else: data["CI"] = max(patients, key=lambda x: x["CI"])["CI"]+1
        patients.append(data)
        return data
    
    @staticmethod
    def update_patient(CI,data):
        patient = PatientsService.find_patients(CI)
        if patient: 
            patient.update(data)
            return patient
        else: 
            return None
        
    @staticmethod
    def delete_patient(CI):
        patient = PatientsService.find_patients(CI)
        if patient:
            patients.remove(patient)
            return patient
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

        if parsed_path.path == "/patients":
            if "diagnostico" in query_params:
                diagnostico = query_params["diagnostico"][0]
                patient_filtred = PatientsService.find_patient_by_diagnostic(
                    diagnostico
                )
                if patient_filtred != []: HTTPResponseHandler.handle_response(self, 200, patient_filtred)
                else: HTTPResponseHandler.handle_response(self, 204, [])
            elif "doctor" in query_params:
                doctor = query_params["doctor"][0]
                patient_filtred = PatientsService.find_patient_by_doctor(
                    doctor
                )
                if patient_filtred != []: HTTPResponseHandler.handle_response(self, 200, patient_filtred)
                else:  HTTPResponseHandler.handle_response(self, 204, [])
            else:
                HTTPResponseHandler.handle_response(self, 200, patients)
                
        elif self.path.startswith("/patients/"):
            id = int(self.path.split("/")[-1])
            patient = PatientsService.find_patients(id)
            if patient: HTTPResponseHandler.handle_response(self, 200, [patient])
            else: HTTPResponseHandler.handle_response(self, 204, {"Error":"patient not found"})
        else: HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_POST(self):
        if self.path == "/patients":
            data = self.read_data()
            patients = PatientsService.add_patient(data)
            HTTPResponseHandler.handle_response(self, 201, patients)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_PUT(self):
        if self.path.startswith("/patients/"):
            CI = int(self.path.split("/")[-1])
            data = self.read_data()
            patients = PatientsService.update_patient(CI, data)
            if patients:
                HTTPResponseHandler.handle_response(self, 200, patients)
            else:
                HTTPResponseHandler.handle_response(
                    self, 404, {"Error": "Estudiante no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_DELETE(self):
        
        if self.path.startswith("/patients/"):
            CI = int(self.path.split("/")[-1])
            patient = PatientsService.delete_patient(CI)
            if patient:
                HTTPResponseHandler.handle_response(self, 200, [patient])
            else:
                HTTPResponseHandler.handle_response(self, 404, "Patient not found")
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