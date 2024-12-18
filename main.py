from mangum import Mangum
from fastapi import FastAPI, HTTPException, Response

app = FastAPI()

@app.get("/api/v1/test")
def test():
    return "Hello, World"

@app.get("/")
def heartbeat():
    return "Success"

@app.get("/404")
def not_found():
    raise HTTPException(status_code=404, detail="Resource not found")

@app.get("/302")
def found(response: Response):
    response.status_code = 302
    response.headers["Location"] = "https://example.com"
    return {"message": "Redirecting to https://example.com"}

@app.get("/500")
def internal_server_error():
    raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/401")
def unauthorized():
    raise HTTPException(status_code=401, detail="Unauthorized")

handler = Mangum(app)
