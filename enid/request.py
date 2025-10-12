class Request:
    def __init__(self, method, path, headers, body):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body

    @classmethod
    def parse(cls, raw_bytes):
        text = raw_bytes.decode("utf-8")
        lines = text.split("\r\n")
        method, path, _ = lines[0].split(" ")
        headers = {}
        i = 1
        while lines[i]:
            key, val = lines[i].split(": ", 1)
            headers[key.lower()] = val
            i += 1
        body = "\r\n".join(lines[i+1:])
        return cls(method, path, headers, body)
