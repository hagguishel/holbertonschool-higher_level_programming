#!/usr/bin/python3
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            json_string = json.dumps(data)
            self.wfile.write(json_string.encode())

        elif self.path == "/status":
            dic = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            json_dic = json.dumps(dic)
            self.end_headers()
            self.wfile.write(json_dic.encode())


if __name__ == "__main__":
    server = http.server.HTTPServer(("localhost", 8000), SimpleAPIHandler)
    print("Serveur lancé sur http://localhost:8000")
    server.serve_forever()
