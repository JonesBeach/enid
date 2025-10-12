# Temporary shim for development.
# To be replaced by calls to Rust-backed Socket and Connection objects.
import socket

class PyConn:
    def __init__(self, conn):
        self.conn = conn

    def recv(self, n):
        return self.conn.recv(n)

    def send(self, data):
        self.conn.sendall(data)

    def close(self):
        self.conn.close()


class PySocket:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This line helps avoid: OSError: [Errno 98] Address already in use
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(5)

    def accept(self):
        conn, addr = self.sock.accept()
        return PyConn(conn), addr


# Mimic memphis.net API
def listen(addr):
    host, port = addr
    return PySocket(host, port)
