from routes import auth, category, products
from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=['Root'])
def root():
    return {"Welcome": "This is the root of the server!"}

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(category.router, tags=['Categories'], prefix='/api/categories')
app.include_router(products.router, tags=['Products'], prefix='/api/products')

