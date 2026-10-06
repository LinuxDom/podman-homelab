import json
import os
import socket
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

START = time.time()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        body = json.dumps({
            "status": "ok",
            "hostname": socket.gethostname(),
            "uptime_seconds": int(time.time() - START),
            "load_avg": os.getloadavg(),
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
