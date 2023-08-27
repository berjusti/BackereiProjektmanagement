from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection
engine = create_engine('postgresql://user:password@localhost/supplychain') 

# Connect to database
Session = sessionmaker(bind=engine)
session = Session()

# Migration example: Add new table
from sqlalchemy import Table, Column, Integer, String

new_table = Table('ingredients', metadata,
   Column('id', Integer, primary_key=True),
   Column('name', String(50)),
   Column('quantity', Integer)
)

new_table.create(engine)

print("Migration complete!")