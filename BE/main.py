from fastapi import FastAPI

app = FastAPI()


@app.get("/")
#async def root():
def root():
    return {"message": "World"}


@app.get("/home")
def home():
    return {"message": "home"}