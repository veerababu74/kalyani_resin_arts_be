from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema, handler):
        field_schema.update(type="string")
        return field_schema


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    dimensions: Optional[str] = None
    materials: Optional[str] = None
    images: List[str] = []
    is_featured: bool = False
    is_new: bool = False


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    dimensions: Optional[str] = None
    materials: Optional[str] = None
    images: Optional[List[str]] = None
    is_featured: Optional[bool] = None
    is_new: Optional[bool] = None


class ProductInDB(ProductBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}


class ProductResponse(ProductBase):
    id: str = Field(alias="_id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        populate_by_name = True
        from_attributes = True
