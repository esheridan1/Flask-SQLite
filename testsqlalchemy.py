from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Declare a mapping
Base = declarative_base()

# Define a User model (table)
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Add a new user
new_user = User(name="Alice", age=30)
session.add(new_user)

# Commit the transaction
session.commit()

# Query the database
for user in session.query(User).all():
    print(user)

# Close the session
session.close()
