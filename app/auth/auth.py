from auth.auth_user_model import User, users_db, find_user, find_user_db
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl='login')
ALGORITHM = "HS256"


crypt = CryptContext(schemes=["bcrypt"])

@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(404, 'user not found')
    
    user = find_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(403, 'wrong credentials')
    
    token = jwt.encode({"username": user.username,"fullname": user.fullname },'this_is_my_secret', ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}

async def auth_user(token: str = Depends(oauth2)):
    tokenData = jwt.decode(key='this_is_my_secret', algorithms=ALGORITHM, token=token)
    user = find_user(tokenData['username'])

    if not user:
        raise HTTPException(401, 'unauthorized', headers={'WWW-Authenticate': 'Bearer'})
    
    if not user.validated:
        raise HTTPException(401, 'user not validated')
    
    return user

@router.get('/')
async def logged(user: User = Depends(auth_user)):
    return user