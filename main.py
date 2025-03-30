from fastapi import FastAPI
import socket
import uvicorn

app = FastAPI()

@app.get("/whoami")
async def whoami():
    hostname = socket.gethostname()
    return {"hostname": hostname}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081) 