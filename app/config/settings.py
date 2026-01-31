from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List
import os


class Settings(BaseSettings):
    # MongoDB
    mongodb_url: str = (
        "mongodb+srv://veera:veera7474@kalyaniresinarts.7mmmbo5.mongodb.net/kalyani_resin_arts?retryWrites=true&w=majority&appName=kalyaniresinarts"
    )

    # Admin Credentials
    admin_username: str = "admin"
    admin_password: str = "admin123"

    # App Settings
    debug: bool = True
    allowed_origins: str = (
        "http://localhost:3000,http://localhost:5173,https://kalyani-resin-arts.vercel.app"
    )

    # Cloudinary Settings (for image upload)
    cloudinary_cloud_name: str = ""
    cloudinary_api_key: str = ""
    cloudinary_api_secret: str = ""

    @property
    def allowed_origins_list(self) -> List[str]:
        """Parse comma-separated origins into a list"""
        return [origin.strip() for origin in self.allowed_origins.split(",")]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
