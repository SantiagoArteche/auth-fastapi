from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    fullname: str
    validated: bool

class UserDB(User):
    password: str

users_db = {
    'sAAn77': {
        "username": "sAAn77",
        "email": "santiarteche@hotmail.com",
        "fullname": "Santiago Arteche",
        "password": "$2a$12$lapA9CXadMjESqmNOwGzUOpwNfjWTZ4FMDutbu/h3wTqoXZfdLVUW",
        "validated": True
    },
    'rando88': {
        "username": "rando88",
        "email": "rando@random.com",
        "fullname": "Brian Gonzalez",
        "password": "$2a$12$lapA9CXadMjESqmNOwGzUOpwNfjWTZ4FMDutbu/h3wTqoXZfdLVUW",
        "validated": False
    },
}

def find_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
    return False

def find_user(username: str):
    if username in users_db:
        return User(**users_db[username])