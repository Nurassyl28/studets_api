
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.schema import UniqueConstraint
from ..database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    group = Column(String(64), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    avatar_url = Column(String(1024), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint('email', name='uq_students_email'),
    )
