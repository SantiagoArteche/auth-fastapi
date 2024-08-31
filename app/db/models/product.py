from bson import ObjectId
from datetime import datetime
from db.mongo import db
from db.schemas.product import product_schema
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    stock: int
    category: str
    createdAt: str = Field(f"{datetime.now()}")


    async def all():
        all_products_db = db.products.find({})
        all_products = []

        for prod in all_products_db:
           all_products.append(product_schema(prod))

        return all_products
            
    async def get_by_id(id: str):
        product = db.products.find_one({"_id": ObjectId(id)})

        if not product:
            return False
        
        return product_schema(product)

    async def create(prod):
        product = dict(prod)
        del product['id']

        new_prod_id = db.products.insert_one(product).inserted_id
        prod_db = db.products.find_one({"_id": new_prod_id})

        return Product(**product_schema(prod_db))
    
    async def update(id_product, prod):
        update_prod = db.products.find_one_and_update({"_id": ObjectId(id_product)}, 
        { "$set": {"price": prod.price, "name": prod.name, "stock": prod.stock, "category": prod.category}})
        

        if update_prod:
            return product_schema(db.products.find_one({"_id": ObjectId(id_product)}))
        
        return False
    
    async def delete(id_product: str):
        delete_prod = db.products.find_one_and_delete({"_id": ObjectId(id_product)})

        if not delete_prod:
            return False
    
        return True