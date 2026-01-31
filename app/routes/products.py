from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from bson import ObjectId
from datetime import datetime
from app.config.database import get_database
from app.models.product import ProductCreate, ProductUpdate, ProductResponse
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/products", tags=["Products"])


def serialize_product(product) -> dict:
    """Convert MongoDB document to response format"""
    if product:
        product["_id"] = str(product["_id"])
    return product


@router.get("", response_model=List[dict])
async def get_all_products():
    """Get all products"""
    db = get_database()
    products = await db.products.find().sort("created_at", -1).to_list(100)
    return [serialize_product(p) for p in products]


@router.get("/featured", response_model=List[dict])
async def get_featured_products():
    """Get featured products"""
    db = get_database()
    products = (
        await db.products.find({"is_featured": True}).sort("created_at", -1).to_list(10)
    )
    return [serialize_product(p) for p in products]


@router.get("/{product_id}")
async def get_product(product_id: str):
    """Get a single product by ID"""
    db = get_database()

    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    product = await db.products.find_one({"_id": ObjectId(product_id)})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return serialize_product(product)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate, username: str = Depends(verify_credentials)
):
    """Create a new product (Admin only)"""
    db = get_database()

    product_dict = product.model_dump()
    product_dict["created_at"] = datetime.utcnow()
    product_dict["updated_at"] = datetime.utcnow()

    result = await db.products.insert_one(product_dict)
    product_dict["_id"] = str(result.inserted_id)

    return product_dict


@router.put("/{product_id}")
async def update_product(
    product_id: str, product: ProductUpdate, username: str = Depends(verify_credentials)
):
    """Update a product (Admin only)"""
    db = get_database()

    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    update_data = {k: v for k, v in product.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()

    result = await db.products.update_one(
        {"_id": ObjectId(product_id)}, {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = await db.products.find_one({"_id": ObjectId(product_id)})
    return serialize_product(updated_product)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, username: str = Depends(verify_credentials)):
    """Delete a product (Admin only)"""
    db = get_database()

    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    result = await db.products.delete_one({"_id": ObjectId(product_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return None
