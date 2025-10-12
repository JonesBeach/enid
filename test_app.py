from enid import App, Response

app = App()

@app.get("/")
def home(req):
    return Response.text("Hello from Enid (powered by Memphis)")

if __name__ == "__main__":
    app.run()
