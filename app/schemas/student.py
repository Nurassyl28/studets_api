
from pydantic import BaseModel, Field, EmailStr, HttpUrl, field_validator
from typing import Optional

class StudentBase(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., ge=16, le=100)
    group: str = Field(..., min_length=1)
    email: EmailStr
    avatar_url: Optional[HttpUrl] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2)
    age: Optional[int] = Field(None, ge=16, le=100)
    group: Optional[str] = Field(None, min_length=1)
    email: Optional[EmailStr] = None
    avatar_url: Optional[HttpUrl] = None

class StudentOut(StudentBase):
    id: int
    class Config:
        from_attributes = True
