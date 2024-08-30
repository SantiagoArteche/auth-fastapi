from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    id: Optional[int] = 0
    name: str
    price: float
    stock: int
    createdAt: str = Field(datetime.now())


    @staticmethod
    def addProduct(product):
        Product.all_products.append(product)
        return product
    
    @staticmethod
    def deleteProduct(product):
        delete = Product.all_products.remove(product)
        if delete:
            return delete
        return False
    
    @staticmethod
    def updateProduct(product):
        for prod in Product.all_products:
            if(product.id == prod.id):
              Product.all_products.remove(prod)
              Product.all_products.insert(prod.id, product)
              return product
        return False   
    
Product.all_products = []