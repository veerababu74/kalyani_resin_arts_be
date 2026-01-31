from pydantic import BaseModel
from typing import Optional, List


class CarouselSlide(BaseModel):
    image: str
    title: Optional[str] = None
    subtitle: Optional[str] = None


class FeatureCard(BaseModel):
    icon: str = "✨"
    title: str
    description: str


class SiteSettings(BaseModel):
    whatsapp: Optional[str] = None
    instagram: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    about_text: Optional[str] = None
    hero_title: Optional[str] = None
    hero_subtitle: Optional[str] = None
    footer_text: Optional[str] = None


class SettingsUpdate(SiteSettings):
    pass


class CarouselUpdate(BaseModel):
    slides: List[CarouselSlide]


class FeatureCardsUpdate(BaseModel):
    cards: List[FeatureCard]
