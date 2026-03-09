from sqlalchemy import Column,Integer,String,Boolean
from database import Base
class User(Base):
    __tablename__=Users

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,index=True,unique=True)
    
