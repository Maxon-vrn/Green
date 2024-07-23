from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


# Кастом авторизации пользователей
class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    login: str
    email: str
    phone: str
    inn: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    login: str
    password: str
    email: str
    phone: str
    inn: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass