from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from qdrant_client import QdrantClient

class RelationalStorage:
  def __init__(self) -> None:
    self.DATABASE_URL = "postgresql+asyncpg://user:senha@localhost:5432/meubanco"
    self.engine = create_async_engine(self.DATABASE_URL, echo=True)

    self.AsyncSessionLocal = async_sessionmaker(
        bind=self.engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    
  def get_session(self) -> AsyncSession:
    return self.AsyncSessionLocal

class Base(DeclarativeBase):
    pass
  
  
class QdrantStorage:
  def __init__(self) -> None:
    pass