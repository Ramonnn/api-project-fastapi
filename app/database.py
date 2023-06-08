from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os.path import expanduser
from urllib import parse

with open(expanduser('~/.pgpass'), 'r') as f:
    host, port, database, user, password = f.read().split(':')

SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}/fastapi' .format(user,parse.quote(password.strip()), host)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():            
    db = SessionLocal()  
    try:                 
        yield db         
    finally:             
        db.close()       
