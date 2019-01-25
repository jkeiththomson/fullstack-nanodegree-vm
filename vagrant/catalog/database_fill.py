# this code is modeled afer "lotsofmenus.py" frpm the REstaurant Menu app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Instrument

# connect to the database
engine = create_engine('sqlite:///orchestra.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


####################### Woodwind Category ############################

category1 = Category(name="Woodwinds", description="all about woodwinds")
session.add(category1)
session.commit()

instrument1 = Instrument(name="Piccolo", description="all about piccolos", category_id=category1.id)
session.add(instrument1)
session.commit()

instrument2 = Instrument(name="Flute", description="all about flutes", category_id=category1.id)
session.add(instrument2)
session.commit()

instrument3 = Instrument(name="Oboe", description="all about oboes", category_id=category1.id)
session.add(instrument3)
session.commit()

instrument4 = Instrument(name="English Horn", description="all about English horns", category_id=category1.id)
session.add(instrument4)
session.commit()

instrument5 = Instrument(name="Clarinet", description="all about clarinets", category_id=category1.id)
session.add(instrument5)
session.commit()

instrument6 = Instrument(name="Bass Clarinet", description="all about bass clarinets", category_id=category1.id)
session.add(instrument6)
session.commit()

instrument7 = Instrument(name="Bassoon", description="all about bassoons", category_id=category1.id)
session.add(instrument7)
session.commit()

instrument8 = Instrument(name="Contrabassoon", description="all about contrabassoons", category_id=category1.id)
session.add(instrument8)
session.commit()


####################### Brass Category ############################

category2 = Category(name="Brass", description="all about brass")
session.add(category2)
session.commit()

instrument11 = Instrument(name="Horn", description="all about horns", category_id=category2.id)
session.add(instrument11)
session.commit()

instrument12 = Instrument(name="Trumpet", description="all about trumpets", category_id=category2.id)
session.add(instrument12)
session.commit()

instrument12 = Instrument(name="Euphonium", description="all about euphonia", category_id=category2.id)
session.add(instrument12)
session.commit()

instrument12 = Instrument(name="Trombone", description="all about trombones", category_id=category2.id)
session.add(instrument12)
session.commit()

instrument12 = Instrument(name="Tuba", description="all about tubas", category_id=category2.id)
session.add(instrument12)
session.commit()


####################### Strings Category ############################

category3 = Category(name="Strings", description="all about strings")
session.add(category3)
session.commit()

instrument21 = Instrument(name="Violin", description="all about violins", category_id=category3.id)
session.add(instrument21)
session.commit()

instrument22 = Instrument(name="Viola", description="all about violas", category_id=category3.id)
session.add(instrument22)
session.commit()

instrument23 = Instrument(name="Cello", description="all about celli", category_id=category3.id)
session.add(instrument23)
session.commit()

instrument24 = Instrument(name="Double Bass", description="all about double basses", category_id=category3.id)
session.add(instrument24)
session.commit()


####################### Precussion Category ############################

category4 = Category(name="Percussion", description="all about percussion")
session.add(category4)
session.commit()

instrument31 = Instrument(name="Timpani", description="all about timpani", category_id=category4.id)
session.add(instrument31)
session.commit()

instrument32 = Instrument(name="Bass Drum", description="all about bass drum", category_id=category4.id)
session.add(instrument32)
session.commit()

instrument33 = Instrument(name="Snare", description="all about snares", category_id=category4.id)
session.add(instrument33)
session.commit()

instrument34 = Instrument(name="Tom-tom", description="all about tom-toms", category_id=category4.id)
session.add(instrument34)
session.commit()

instrument35 = Instrument(name="Cymbsl", description="all about cymbals", category_id=category4.id)
session.add(instrument35)
session.commit()

instrument36 = Instrument(name="Gong", description="all about gongs", category_id=category4.id)
session.add(instrument36)
session.commit()

instrument37 = Instrument(name="Piano", description="all about pianos", category_id=category4.id)
session.add(instrument37)
session.commit()

instrument38 = Instrument(name="Celeste", description="all about celestes", category_id=category4.id)
session.add(instrument38)
session.commit()

instrument39 = Instrument(name="Harp", description="all about harps", category_id=category4.id)
session.add(instrument39)
session.commit()

print "added categories and instruments!"
