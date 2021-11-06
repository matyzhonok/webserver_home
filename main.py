import api_litlehome

from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if (self.path.startswith("/litlehome/")):
            print("   |-> Распознан запрос к макету")
            api_litlehome.litleHomeApi_main(self, self.path.replace("/litlehome/", "", 1))
            return True
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Server API for SmartHome by Victor Matyzhonok\n')
            self.wfile.write(b"Request api '")
            self.wfile.write(bytes(self.path, "utf-8"))
            self.wfile.write(b"' not recoqnized\n")


httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()