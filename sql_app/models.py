from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# 从 database.py 导入 Base
from .database import Base

'''SQLAlchemy模型'''
# 在SQLAlchemy中，模型 指代与数据库的交互的类和实例

class User(Base):
# __tablename__ 表名
    __tablename__ = "users"

# 传递SQL数据类型：Integer, String, Boolean ...
# 设置 primary key, 是否唯一 unique, 设置索引index, 设置默认值 default
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

# 用 SQLAlchemy ORM 提供的 relationship 创建关系
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")