from bson import ObjectId
from db.mongo import db
from db.schemas.user import user_schema
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    password: str
    

    def find_by_email(email: str):
        db_user = db.users.find_one({"email": email})

        if not db_user:
            return False

        return db_user
    
    def find_by_username(username: str):
        db_user = db.users.find_one({"username": username})

        if not db_user:
            return False

        return db_user

    async def create(user):
            crypt = CryptContext(schemes=["bcrypt"])

            existByEmail, existByUsername = User.find_by_email(user.email), User.find_by_username(user.username)
            
            if existByEmail or existByUsername:
                 return False

            user_dict = dict(user)
            del user_dict["id"]
       
            user_dict["password"] = crypt.hash(f"{user_dict["password"]}")
            user_id = db.users.insert_one(user_dict).inserted_id

            new_user = user_schema(db.users.find_one({"_id": user_id}))
            return User(**new_user)
    
    async def delete(id_user: str):
        delete_user = db.users.find_one_and_delete({"_id": ObjectId(id_user)})

        if not delete_user:
            return False
        
        return True