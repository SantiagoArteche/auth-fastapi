from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Final

class Product(BaseModel):
    id: Optional[int] = 0
    name: str
    price: float
    stock: int
    category: str
    createdAt: str = Field(f"{datetime.now()}")
    all_products: Final[list] = []
    
    def addProduct(product):
        Product.all_products.append(product)
        return product
    
    def deleteProduct(product):
        delete = Product.all_products.remove(product)
        if delete:
            return delete
        return False
    
    def updateProduct(product):
        for prod in Product.all_products:
            if product.id == prod.id:
                Product.all_products.remove(prod)
                Product.all_products.insert(prod.id, product)
                return product
            
        return False   
 