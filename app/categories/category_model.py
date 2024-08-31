from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Final

class Category(BaseModel):
    id: Optional[int] = 0
    name: str
    createdAt: str = Field(f"{datetime.now()}")

    all_categories: Final[list] = []

    def getAll():
        return Category.all_categories

    def getById(id):
        for category in Category.all_categories:
            if id == category.id:
                return category
            
        return False

    def createCategory(category):
        Category.all_categories.append(category)
        return category
    
    def deleteCategory(id):
        for category in Category.all_categories:
            if id == category.id:
                Category.all_categories.remove(category)
                return True

        return False
                
    def updateById(id, updatedValues):
        for category in Category.all_categories:
            if id == category.id:
                Category.all_categories.remove(category)
                Category.all_categories.insert(category.id, updatedValues)
                return True
            
        return False