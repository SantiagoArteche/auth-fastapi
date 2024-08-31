from fastapi import APIRouter, HTTPException
from products.product_model import Product

router = APIRouter()

@router.get('/')
async def getAllProducts():
    try:
        return {"products": Product.all_products}
    except:
        raise HTTPException(status_code=500, detail=f"Internal Server Error")

@router.get("/{id}", response_model=Product)
async def getProductById(id: int):
    product = filter(lambda prod: prod.id == id, Product.all_products)
    print(product)
    try:
        return list(product)[0]
    except:
        raise HTTPException(status_code=404, detail=f"product with id {id} not found")
   
    
@router.post('/', status_code=201)
async def createProduct(prod: Product):
    if len(Product.all_products) == 0:
        id = 0
    else:
        id = Product.all_products[-1].id + 1
        
    newProd = Product(id=id, name=prod.name, stock=prod.stock, price=prod.price, category=prod.category)
    try:
        Product.addProduct(newProd)
        return {"msg": "product created!", "product": newProd}
    except:
        raise HTTPException(status_code=400, detail=f"error in creation")
    
@router.put('/{id}')
async def updateProduct(prod: Product, id: int):
        newValues = Product(id=+id, category=prod.category, name=prod.name, stock=prod.stock, price=prod.price)
        updatedProduct = Product.updateProduct(newValues)
            
        if not updatedProduct:
            raise HTTPException(status_code=404, detail=f"product with id {id} not found")
            
        return {"msg": "Updated product!", "Product": updatedProduct}

@router.delete('/{id}')
async def deleteProduct(id: int):
    product = filter(lambda prod: prod.id == id, Product.all_products)

    try:
        Product.deleteProduct(list(product)[0])
        return {"msg": f"product with id {id} was deleted!"}
    except:
        raise HTTPException(status_code=404, detail=f"product with id {id} not found")

