from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
import cloudinary
import cloudinary.uploader
from app.config.settings import settings
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/upload", tags=["Upload"])

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret,
)


@router.post("")
async def upload_image(
    file: UploadFile = File(...), username: str = Depends(verify_credentials)
):
    """Upload an image to Cloudinary (Admin only)"""

    # Validate file type
    allowed_types = ["image/jpeg", "image/png", "image/webp", "image/gif"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400, detail="Invalid file type. Allowed: JPEG, PNG, WebP, GIF"
        )

    # Validate file size (max 5MB)
    contents = await file.read()
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400, detail="File too large. Maximum size is 5MB"
        )

    try:
        # Upload to Cloudinary
        result = cloudinary.uploader.upload(
            contents,
            folder="kalyani_resin_arts",
            resource_type="image",
            transformation=[
                {"width": 1200, "height": 1200, "crop": "limit"},
                {"quality": "auto:good"},
            ],
        )

        return {
            "url": result["secure_url"],
            "public_id": result["public_id"],
            "width": result.get("width"),
            "height": result.get("height"),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")


@router.delete("/{public_id:path}")
async def delete_image(public_id: str, username: str = Depends(verify_credentials)):
    """Delete an image from Cloudinary (Admin only)"""
    try:
        result = cloudinary.uploader.destroy(public_id)
        if result.get("result") == "ok":
            return {"message": "Image deleted successfully"}
        else:
            raise HTTPException(status_code=400, detail="Failed to delete image")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete image: {str(e)}")
