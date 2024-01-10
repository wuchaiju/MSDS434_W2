import http.server
import socketserver

PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

witf socketserver.TCPServer(("MSDS434MSDS434_ModuleTwo", PORT), ler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
