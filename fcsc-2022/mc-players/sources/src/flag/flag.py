from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'FCSC{TEST_FLAG}')
        exit(0)

httpd = HTTPServer(('0.0.0.0', 1337), SimpleHTTPRequestHandler)
httpd.serve_forever()
