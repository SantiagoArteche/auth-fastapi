from fastapi import FastAPI
from products import products

app = FastAPI()


@app.get("/", tags=['Root'])
def root():
    return {"Welcome": "This is the start of the server!"}

app.include_router(products.router, tags=['Products'], prefix='/api/products')

