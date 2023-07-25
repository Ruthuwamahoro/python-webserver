#creating my simple HTTP server
import http.server
class CGIRequestHandler(http.server.CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path =='/':
            self.path = 'index.html'
        elif self.path == '/page':
            self.path = '/cgi-bin/page.py'
        return http.server.CGIHTTPRequestHandler.do_GET(self)
handler = CGIRequestHandler
PORT = 5000 #specifies the port on which the server will listen for incoming HTTP requests.
try:
    with http.server.HTTPServer(("0.0.0.0", PORT), handler) as server:
        print("server started at port: " , PORT)
        server.serve_forever()#This starts the HTTP server to listen for incoming requests indefinitely. The server will continue running until you manually stop it
except KeyboardInterrupt:
    print("server stopped")