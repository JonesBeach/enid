# enid
A micro HTTP framework for the [Memphis](https://github.com/JonesBeach/memphis) Python engine.

## Example

Enid's usage is inspired by Flask, and designed to work within the constraints of the Memphis engine. ([See the supported features.](https://github.com/JonesBeach/memphis/blob/main/docs/SUPPORTED.md))
```python
from enid import App, Response

app = App()

@app.get("/")
def home(req):
    return Response.text("Hello from Enid (powered by Memphis)")

if __name__ == "__main__":
    app.run()
```

## Running
You can run an Enid app on either CPython or Memphis.
```bash
memphis test_app.py
# or
python3 test_app.py
```
And test with:
```bash
curl localhost:8080
```
