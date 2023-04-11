from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
Base = declarative_base()


class Calendar(Base):
    __tablename__ = "calendar"
    id = Column('id',Integer, primary_key=True)
    title = Column('title',String(100), nullable=False)
    start = Column('start',date, default=date, nullable=True)
    end = Column('end',date, default=date, nullable=True)

    def __init__(self,id,title,start,end):
        self.id = id
        self.title = title
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.id}) {self.title} {self.start} {self.end}"
    
engine = create_engine('sqlite:///test4.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()