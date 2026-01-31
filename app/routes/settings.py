from fastapi import APIRouter, Depends
from typing import List
from app.config.database import get_database
from app.models.settings import SiteSettings, CarouselSlide, FeatureCard
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("")
async def get_settings():
    """Get site settings"""
    db = get_database()
    settings = await db.settings.find_one({"type": "site_settings"})

    if not settings:
        # Return default settings
        return SiteSettings().model_dump()

    return {
        "whatsapp": settings.get("whatsapp", ""),
        "instagram": settings.get("instagram", ""),
        "email": settings.get("email", ""),
        "address": settings.get("address", ""),
        "about_text": settings.get("about_text", ""),
        "hero_title": settings.get("hero_title", ""),
        "hero_subtitle": settings.get("hero_subtitle", ""),
        "footer_text": settings.get("footer_text", ""),
    }


@router.put("")
async def update_settings(
    settings_data: SiteSettings, username: str = Depends(verify_credentials)
):
    """Update site settings (Admin only)"""
    db = get_database()

    await db.settings.update_one(
        {"type": "site_settings"},
        {"$set": {**settings_data.model_dump(), "type": "site_settings"}},
        upsert=True,
    )

    return settings_data


@router.get("/carousel")
async def get_carousel():
    """Get carousel slides"""
    db = get_database()
    carousel = await db.settings.find_one({"type": "carousel"})

    if not carousel:
        return []

    return carousel.get("slides", [])


@router.put("/carousel")
async def update_carousel(
    slides: List[CarouselSlide], username: str = Depends(verify_credentials)
):
    """Update carousel slides (Admin only)"""
    db = get_database()

    slides_data = [slide.model_dump() for slide in slides]

    await db.settings.update_one(
        {"type": "carousel"},
        {"$set": {"type": "carousel", "slides": slides_data}},
        upsert=True,
    )

    return slides_data


@router.get("/features")
async def get_features():
    """Get feature cards for About section"""
    db = get_database()
    features = await db.settings.find_one({"type": "features"})

    if not features:
        # Return default feature cards
        return [
            {
                "icon": "🎨",
                "title": "Handcrafted",
                "description": "Every piece is made by hand with attention to detail",
            },
            {
                "icon": "✨",
                "title": "Unique Designs",
                "description": "No two pieces are exactly alike - each is one of a kind",
            },
            {
                "icon": "💎",
                "title": "Premium Quality",
                "description": "We use only the finest resin and materials",
            },
            {
                "icon": "🎁",
                "title": "Perfect Gifts",
                "description": "Ideal for special occasions and loved ones",
            },
            {
                "icon": "🌿",
                "title": "Eco-Friendly",
                "description": "We use sustainable and eco-conscious materials",
            },
            {
                "icon": "💝",
                "title": "Made with Love",
                "description": "Each creation carries our passion and dedication",
            },
        ]

    return features.get("cards", [])


@router.put("/features")
async def update_features(
    cards: List[FeatureCard], username: str = Depends(verify_credentials)
):
    """Update feature cards (Admin only)"""
    db = get_database()

    cards_data = [card.model_dump() for card in cards]

    await db.settings.update_one(
        {"type": "features"},
        {"$set": {"type": "features", "cards": cards_data}},
        upsert=True,
    )

    return cards_data
