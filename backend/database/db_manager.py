from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DBManager(Base):

    __tablename__ = "flip data"
    id = Column("id", Integer, primary_key=True)
    current_state = Column("state", Integer, primary_key=False)
    num_of_clicks = Column("clicks", Integer, primary_key=False)

    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flipdata.db'
        self.db = SQLAlchemy(app)

    #def init_table():
        
    