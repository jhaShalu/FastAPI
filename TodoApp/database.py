from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # 'postgresql://user:password@localhost/databaseName'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/TodoApplicationDatabase' # 'postgresql://user:password@localhost/databaseName'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()