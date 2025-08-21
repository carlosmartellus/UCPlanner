from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///data/ucplanner.db', echo=False)
SessionLocal = sessionmaker(bind=engine)
