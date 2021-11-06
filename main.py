from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        self.wfile.write(bytes(self.path, "utf-8"))


httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()