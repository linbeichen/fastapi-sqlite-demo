from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None

# 如果有其他需要的属性可以加
# 但是ItemCreate 继承了 ItemBase的所有字段
class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True