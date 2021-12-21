from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

SQLALCHEMY_DATABASE_URL = "sqlite:///databases/sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=3600,
    connect_args={"check_same_thread": False},
    poolclass=NullPool
)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine
                            )

Base = declarative_base()
