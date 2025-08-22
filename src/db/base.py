import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_dir = "data"
os.makedirs(db_dir, exist_ok=True)

Base = declarative_base()
db_path = os.path.join(db_dir, "ucplanner.db")
engine = create_engine(f"sqlite:///{db_path}", echo=False)
SessionLocal = sessionmaker(bind=engine)
