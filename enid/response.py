class Response:
    def __init__(self, body, status=200, headers=None):
        self.body = body
        self.status = status
        self.headers = headers or {}

    @classmethod
    def text(cls, text, status=200):
        return cls(text, status, {"Content-Type": "text/plain"})

    def to_bytes(self):
        headers = [f"{k}: {v}" for k, v in self.headers.items()]
        joined = "\r\n".join(headers)
        return (
            f"HTTP/1.1 {self.status} OK\r\n{joined}\r\n\r\n{self.body}"
        ).encode("utf-8")
