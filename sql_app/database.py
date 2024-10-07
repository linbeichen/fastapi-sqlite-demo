from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal类的实例是实际的数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 类，每个数据库模型或类（ORM模型）都会继承这个类
Base = declarative_base()

