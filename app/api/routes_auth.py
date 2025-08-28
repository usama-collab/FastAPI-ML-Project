from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_access_token


router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str


@router.post('/login')
def login(auth: AuthInput):
    if (auth.username == 'admin') and (auth.password == 'admin'):
        token = create_access_token({'sub': auth.username})
        return {'access_token': token}
    return {'message': 'Invalid Credentials'}