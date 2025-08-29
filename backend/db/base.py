from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///ucplanner.db", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
