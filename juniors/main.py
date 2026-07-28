import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", 3000))


class Handler(BaseHTTPRequestHandler):
    def responder(self):
        corpo = json.dumps({"status": "ok"}).encode()
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    do_GET = responder
    do_POST = responder

    def log_message(self, *args):
        pass  # silencia o log por request — sob carga ele vira gargalo


# O '0.0.0.0' é obrigatório — sem ele o container sobe mas não responde de fora.
print(f"ouvindo na porta {PORT}", flush=True)
ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
