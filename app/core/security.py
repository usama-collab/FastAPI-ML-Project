from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from app.core.config import settings

def create_access_token(data: dict, expire_time=15):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_time)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    
def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        return payload
    except JWTError:
        return None
