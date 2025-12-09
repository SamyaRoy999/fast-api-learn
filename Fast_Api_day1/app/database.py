from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "root"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost:5433/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()