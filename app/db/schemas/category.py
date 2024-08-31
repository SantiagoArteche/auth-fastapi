def category_schema(category) -> dict:
    return {
        "id": str(category['_id']),
        "name": category['name'],
        "createdAt": category['createdAt']
    }