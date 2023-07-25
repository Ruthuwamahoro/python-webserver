#creating my simple HTTP server
import http.server
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
handler = RequestHandler
PORT = 5000 #specifies the port on which the server will listen for incoming HTTP requests.
try:
    with http.server.HTTPServer(("0.0.0.0", PORT), handler) as server:
        print("server started at port: " , PORT)
        server.serve_forever()#This starts the HTTP server to listen for incoming requests indefinitely. The server will continue running until you manually stop it
except KeyboardInterrupt:
    print("server stopped")
