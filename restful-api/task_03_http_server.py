#!/usr/bin/python3
"""ficher test"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """class"""

    def do_GET(self):
        """def test"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            json_string = json.dumps(data)
            self.wfile.write(json_string.encode())

        elif self.path == "/status":
            dic = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            json_dic = json.dumps(dic)
            self.end_headers()
            self.wfile.write(json_dic.encode())

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("localhost", 8000), SimpleAPIHandler)
    print("Serveur lancé sur http://localhost:8000")
    server.serve_forever()
