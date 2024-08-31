from db.models.user import User
from db.mongo import db
from db.schemas.user import user_schema
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')
ALGORITHM = "HS256"
crypt = CryptContext(schemes=["bcrypt"])

@router.post('/')
async def create_user(user: User):
    newUser = await User.create(user)

    if not newUser:
        raise HTTPException(400, 'user already exists by that email or username')
    
    return newUser

@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = db.users.find_one({"username": form.username})
    if not user_db:
        raise HTTPException(404, 'user not found')
    
    user = User(**user_schema(user_db))

    if not crypt.verify(form.password, user.password):
        raise HTTPException(403, 'wrong credentials')
    
    token = jwt.encode({"username": user.username,"id": user.id },'this_is_my_secret', ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}

async def auth_user(token: str = Depends(oauth2)):
    token_data = jwt.decode(key='this_is_my_secret', algorithms=ALGORITHM, token=token)
    user = db.users.find_one({"username": token_data['username']})

    if not user:
        raise HTTPException(401, 'unauthorized', headers={'WWW-Authenticate': 'Bearer'})
    
    return User(**user_schema(user))

@router.get('/')
async def login_response(user: User = Depends(auth_user)):
    return {"id": user.id, "username": user.username, "msg": 'Successfull login!'}

@router.delete('/{id}')
async def delete_user(id: str):
    deleted_user = await User.delete(id)
    
    if not deleted_user:
        raise HTTPException(404, 'user not found')
    
    return {f'User with id {id} was deleted!'}