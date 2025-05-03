from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Config

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{Config.db_user}:{Config.db_password}@{Config.db_host}:{Config.db_port}/{Config.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
