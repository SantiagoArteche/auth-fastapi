from auth import auth
from categories import category
from fastapi import FastAPI
from products import products

app = FastAPI()

@app.get("/", tags=['Root'])
def root():
    return {"Welcome": "This is the root of the server!"}

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(category.router, tags=['Categories'], prefix='/api/categories')
app.include_router(products.router, tags=['Products'], prefix='/api/products')

