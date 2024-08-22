from fastapi import FastAPI

"""
uvicorn main:app --reload

http://127.0.0.1:8000/docs
https://fastapi.tiangolo.com/zh/
"""

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
