from bson import ObjectId
from datetime import datetime
from db.mongo import db
from db.schemas.category import category_schema
from pydantic import BaseModel, Field
from typing import Optional

class Category(BaseModel):
    id: Optional[str] = None
    name: str
    createdAt: str = Field(f"{datetime.now()}")

    async def all():
        all_categories_db = db.categories.find({})
        all_categories = []

        for category in all_categories_db:
           all_categories.append(category_schema(category))

        return all_categories
            
    async def get_by_id(id: str):
        category = db.categories.find_one({"_id": ObjectId(id)})

        if not category:
            return False
        
        return category_schema(category)

    async def create(categ):
        category = dict(categ)
        del category['id']
    
        new_cat_id = db.categories.insert_one(category).inserted_id
        category_db = db.categories.find_one({"_id": new_cat_id})
        return Category(**category_schema(category_db))
    
    async def update(id_category, prod):
        update_category = db.categories.find_one_and_update({"_id": ObjectId(id_category)}, 
        { "$set": {"name": prod.name}})
        

        if update_category:
            return category_schema(db.categories.find_one({"_id": ObjectId(id_category)}))
        
        return False
    
    async def delete(id_category: str):
        delete_category = db.categories.find_one_and_delete({"_id": ObjectId(id_category)})

        if not delete_category:
            return False
    
        return True