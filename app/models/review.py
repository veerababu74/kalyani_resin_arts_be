from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ReviewBase(BaseModel):
    customer_name: str = Field(..., min_length=1, max_length=100)
    customer_image: Optional[str] = None
    rating: int = Field(..., ge=1, le=5)
    review_text: str = Field(..., min_length=1, max_length=500)
    product_name: Optional[str] = None
    is_featured: bool = False


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_image: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    review_text: Optional[str] = None
    product_name: Optional[str] = None
    is_featured: Optional[bool] = None


class ReviewResponse(ReviewBase):
    id: str
    created_at: datetime
