from db.models.product import Product
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
async def get_all():
    all_products = await Product.all()
    
    try:
        return {"products": all_products}
    except:
        raise HTTPException(status_code=500, detail=f"Internal Server Error")

@router.get("/{id}")
async def get_by_id(id: str):
    try:
        product_by_id = await Product.get_by_id(id)

        if not product_by_id:
            raise HTTPException(status_code=404, detail=f"product with id {id} not found")
        
        return product_by_id   
    except:
        raise HTTPException(status_code=404, detail=f"product with id {id} not found")

    
@router.post('/', status_code=201)
async def create_product(prod: Product):
    new_prod = await Product.create(prod)
    try:
        return {"msg": "product created!", "product": new_prod}
    except:
        raise HTTPException(status_code=400, detail=f"error in creation")
    
@router.put('/{id}')
async def update_product(prod: Product, id: str):
        updated_product = await Product.update(id, prod)

        if not updated_product:
            raise HTTPException(status_code=404, detail=f"product with id {id} not found")
            
        return {"msg": "Updated product!", "Product": updated_product}

@router.delete('/{id}')
async def delete_product(id: str):
    try:
        deleted_prod = await Product.delete(id)
        
        if not deleted_prod:
            raise HTTPException(404, 'product not found')
        
        return {f'Product with id {id} was deleted!'}
    except:
        raise HTTPException(404, 'product not found')

