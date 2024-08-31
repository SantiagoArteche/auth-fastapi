from categories.category_model import Category
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get('/')
async def getAllCategories():
    return {"categories": Category.getAll()}

@router.get('/{id}')
async def getCategoryById(id: int):
    category = Category.getById(id)
    if category:
        return {"category": category}
    else:
        raise HTTPException(404, 'category not found')

@router.post('/')
async def createCategory(category: Category):
    exists = filter(lambda newCategory: newCategory.name == category.name, Category.all_categories)
    if(list(exists).__len__()):
        raise HTTPException(400, 'Category already exists')

    if not len(Category.all_categories):
        id = 0
    else:
        id = Category.all_categories[-1].id + 1
    
    newCategory = Category(id=id, name=category.name)

    try:
        category = Category.createCategory(newCategory)
        return {"msg": "Category created!", "category": category}
    except:
        raise HTTPException(400, 'bad request')
    

@router.put('/{id}')
async def updateCategory(category: Category, id: int):
    category = Category(id=id,name=category.name)
    updatedCategory = Category.updateById(id, category)

    if not updatedCategory:
        raise HTTPException(400, 'not found')

    return {"msg": "Category updated", "category": category}


@router.delete('/{id}')
async def deleteCategory(id: int):
    delete = Category.deleteCategory(id)

    if not delete:
        raise HTTPException(404, 'category not found')

    return {f"Category with id {id} was deleted!"}

