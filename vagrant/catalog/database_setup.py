# set up the initial database
import os
import sys
import json
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# ------------------ Category table ---------------------
class Category(Base):
    __tablename__ = 'category'

    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(1200), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
        }


# ---------------- Instrument table --------------------
class Instrument(Base):
    __tablename__ = 'instrument'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(1200))
    picture_url = Column(String(250))
    picture_attr = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'picture_url': self.picture_url,
            'picture_attr': self.picture_attr,
            'category_id': self.category_id,
        }


# create the database
engine = create_engine(
    'sqlite:///orchestra.db',
    connect_args={'check_same_thread': False})

# create the tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# prepare to load the data
DBSession = sessionmaker(bind=engine)
session = DBSession()

# get the category data from JSON file
with open('database_categories.json') as cat_file:
    cat_data = json.load(cat_file)
    cats = cat_data["Categories"]
    for c in cats:
        category = Category(name=c["name"],
                            description=c["description"])
        session.add(category)
        session.commit()

# get the instrument data from JSON file
with open('database_instruments.json') as inst_file:
    inst_data = json.load(inst_file)
    insts = inst_data["Instruments"]
    for i in insts:
        # find categpry id for this instrument
        instrument = Instrument(name=i["name"],
                                description=i["description"],
                                category_id=i["category_id"],
                                picture_url=i["picture_url"],
                                picture_attr=i["picture_attr"])
        session.add(instrument)
        session.commit()

# finish up
print "orchestra.db has been set up!"
