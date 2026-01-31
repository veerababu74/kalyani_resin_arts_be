from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from bson import ObjectId
from datetime import datetime
from app.config.database import get_database
from app.models.review import ReviewCreate, ReviewUpdate, ReviewResponse
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/reviews", tags=["Reviews"])


def serialize_review(review) -> dict:
    """Convert MongoDB document to response format"""
    if review:
        review["_id"] = str(review["_id"])
    return review


@router.get("", response_model=List[dict])
async def get_all_reviews():
    """Get all reviews"""
    db = get_database()
    reviews = await db.reviews.find().sort("created_at", -1).to_list(100)
    return [serialize_review(r) for r in reviews]


@router.get("/featured", response_model=List[dict])
async def get_featured_reviews():
    """Get featured reviews for homepage"""
    db = get_database()
    reviews = (
        await db.reviews.find({"is_featured": True}).sort("created_at", -1).to_list(10)
    )
    return [serialize_review(r) for r in reviews]


@router.get("/{review_id}")
async def get_review(review_id: str):
    """Get a single review by ID"""
    db = get_database()

    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid review ID")

    review = await db.reviews.find_one({"_id": ObjectId(review_id)})

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return serialize_review(review)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_review(
    review: ReviewCreate, username: str = Depends(verify_credentials)
):
    """Create a new review (Admin only)"""
    db = get_database()

    review_dict = review.model_dump()
    review_dict["created_at"] = datetime.utcnow()
    review_dict["updated_at"] = datetime.utcnow()

    result = await db.reviews.insert_one(review_dict)
    review_dict["_id"] = str(result.inserted_id)

    return review_dict


@router.put("/{review_id}")
async def update_review(
    review_id: str, review: ReviewUpdate, username: str = Depends(verify_credentials)
):
    """Update a review (Admin only)"""
    db = get_database()

    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid review ID")

    update_data = {k: v for k, v in review.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()

    result = await db.reviews.update_one(
        {"_id": ObjectId(review_id)}, {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Review not found")

    updated_review = await db.reviews.find_one({"_id": ObjectId(review_id)})
    return serialize_review(updated_review)


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(review_id: str, username: str = Depends(verify_credentials)):
    """Delete a review (Admin only)"""
    db = get_database()

    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid review ID")

    result = await db.reviews.delete_one({"_id": ObjectId(review_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Review not found")
