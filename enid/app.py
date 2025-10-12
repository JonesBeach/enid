try:
    from memphis.net import listen
except ImportError:
    # Fallback to the pure-Python shim
    from .shim_net import listen

from .request import Request
from .response import Response

class App:
    def __init__(self):
        self.routes = {}

    def route(self, path, methods=["GET"]):
        def decorator(fn):
            for m in methods:
                self.routes[(path, m)] = fn
            return fn
        return decorator

    def get(self, path):
        return self.route(path, ["GET"])

    def post(self, path):
        return self.route(path, ["POST"])

    def run(self, host="127.0.0.1", port=8080):
        sock = listen((host, port))
        print(f"Serving on {host}:{port}")
        while True:
            conn, _ = sock.accept()
            req = Request.parse(conn.recv(4096))
            handler = self.routes.get((req.path, req.method))
            if not handler:
                conn.send(Response.text("404 Not Found", status=404).to_bytes())
            else:
                res = handler(req)
                conn.send(res.to_bytes())
            conn.close()
