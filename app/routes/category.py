from db.models.category import Category
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
async def get_all():
    try:
        all_categories = await Category.all()
        return {"categories": all_categories}
    except:
        raise HTTPException(status_code=500, detail=f"server error")

@router.get('/{id}')
async def get_category(id: str):
    category = await Category.get_by_id(id)
    if category:
        return {"category": category}
    else:
        raise HTTPException(404, 'category not found')

@router.post('/')
async def create_category(category: Category):
    new_prod = await Category.create(category)
    try:
        return {"msg": "product created!", "product": new_prod}
    except:
        raise HTTPException(status_code=400, detail=f"error in creation")
    

@router.put('/{id}')
async def update_category(category: Category, id: str):
        updated_category = await Category.update(id, category)

        if not updated_category:
            raise HTTPException(status_code=404, detail=f"product with id {id} not found")
            
        return {"msg": "Updated product!", "Product": updated_category}


@router.delete('/{id}')
async def delete_category(id: str):
    delete = await Category.delete(id)

    if not delete:
        raise HTTPException(404, 'category not found')

    return {f"Category with id {id} was deleted!"}

