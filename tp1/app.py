from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            # Un gros gif de chat
            self.wfile.write(b"""
            <h1>Wild Kitty Override!</h1>
            <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" alt="kitty gif">
            """)
        else:
            self.send_error(404)

if __name__ == '__main__':
    server = HTTPServer(('', 8000), Handler)
    print("Serving on port 8000…")
    server.serve_forever()