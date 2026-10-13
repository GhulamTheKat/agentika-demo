from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Agentika 2.0 Demo Deployment is Live!"}
