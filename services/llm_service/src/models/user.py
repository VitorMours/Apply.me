from sqlalchemy.orm import Mapped, mapped_column 
from core.database import Base
from uuid import uuid

class User(Base):
  __tablename__ = "users"
  id: Mapped[uuid] = mapped_column(primary_key=True)
  firstName: Mapped[str]
  lastName: Mapped[str]
  email: Mapped[str] = mapped_column(unique=True)
  # createdat
  # updateat
  