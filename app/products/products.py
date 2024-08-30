from products.product_model import Product
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def getAllProducts():
    try:
        return {"products": Product.all_products}
    except:
        return {"error": f"Server error"}

@router.get("/{id}")
async def getProductById(id: int):
    product = filter(lambda prod: findProduct(prod, id), Product.all_products)

    try:
        return list(product)[0]
    except:
        return {"error": f"product with id {id} not found"}
    
@router.post('/', status_code=201)
async def createProduct(prod: Product):
    newProd = Product(id=Product.all_products.__len__(), name=prod.name, stock=prod.stock, price=prod.price)
    try:
        Product.addProduct(newProd)
        return {"msg": "product created!", "product": newProd}
    except:
        return {"error": f"Error in the creation"}
    

@router.put('/{id}')
def updateProduct(prod: Product, id: int):
        newValues = Product(id=+id, name=prod.name, stock=prod.stock, price=prod.price)
        updatedProduct = Product.updateProduct(newValues)
        
        if(updatedProduct):
            return {"msg": "Updated product!", "Product": updatedProduct}
        else:
            return {"error": f"product with id {id} not found"}


    
@router.delete('/{id}')
def deleteProduct(id: int):
    product = filter(lambda prod: findProduct(prod, id), Product.all_products)
    try:
        Product.deleteProduct(list(product)[0])
        return {"msg": f"product with id {id} was deleted!"}
    except:
        return {"error": f"Product with id {id} not found"}


def findProduct(product, id):
    return product.id == id