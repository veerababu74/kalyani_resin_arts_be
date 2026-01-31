"""
Seed script to populate database with dummy products
Run: python seed_data.py
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

# MongoDB connection
MONGODB_URL = "mongodb+srv://veera:veera7474@kalyaniresinarts.7mmmbo5.mongodb.net/kalyani_resin_arts?retryWrites=true&w=majority&appName=kalyaniresinarts"

# Sample product images (using placeholder images)
sample_images = [
    "https://images.unsplash.com/photo-1616627577385-5c0c4dab4a3d?w=500",
    "https://images.unsplash.com/photo-1617791160505-6f00504e3519?w=500",
    "https://images.unsplash.com/photo-1615486511484-92e172cc4fe0?w=500",
    "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?w=500",
    "https://images.unsplash.com/photo-1596162954151-cdcb4c0f70a8?w=500",
]

# Dummy products data
products = [
    {
        "name": "Ocean Wave Coaster Set",
        "description": "Beautiful handcrafted resin coasters with ocean wave design. Each piece captures the essence of the sea with swirling blues and whites. Perfect for home décor or as a thoughtful gift.",
        "price": 899,
        "category": "Coasters",
        "dimensions": "10cm x 10cm (Set of 4)",
        "materials": "Epoxy resin, blue pigments, white pigments, gold flakes",
        "images": [
            "https://images.unsplash.com/photo-1616627577385-5c0c4dab4a3d?w=500",
            "https://images.unsplash.com/photo-1617791160505-6f00504e3519?w=500",
            "https://images.unsplash.com/photo-1615486511484-92e172cc4fe0?w=500",
        ],
        "is_featured": True,
        "is_new": True,
    },
    {
        "name": "Galaxy Pendant Necklace",
        "description": "Stunning galaxy-themed pendant made with premium resin. Features deep purple and blue hues with shimmering stars. Comes with a silver chain.",
        "price": 599,
        "category": "Jewelry",
        "dimensions": "3cm diameter",
        "materials": "Crystal clear resin, holographic glitter, silver chain",
        "images": [
            "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500",
        ],
        "is_featured": True,
        "is_new": False,
    },
    {
        "name": "Floral Bookmark Collection",
        "description": "Elegant bookmarks with preserved real flowers encased in crystal-clear resin. Each bookmark is unique with hand-picked dried flowers.",
        "price": 349,
        "category": "Bookmarks",
        "dimensions": "15cm x 4cm",
        "materials": "UV resin, dried flowers, gold leaf",
        "images": [
            "https://images.unsplash.com/photo-1544967082-d9d25d867d66?w=500",
            "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=500",
        ],
        "is_featured": False,
        "is_new": True,
    },
    {
        "name": "Sunset Mountain Wall Art",
        "description": "Breathtaking wall art piece featuring a sunset mountain landscape. Hand-poured layers create a stunning 3D effect with warm orange and purple tones.",
        "price": 2499,
        "category": "Wall Art",
        "dimensions": "30cm x 40cm",
        "materials": "Epoxy resin, acrylic pigments, wood frame",
        "images": [
            "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=500",
            "https://images.unsplash.com/photo-1549887534-1541e9326642?w=500",
            "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=500",
        ],
        "is_featured": True,
        "is_new": False,
    },
    {
        "name": "Crystal Clear Trinket Tray",
        "description": "Elegant trinket tray perfect for storing jewelry, keys, or small accessories. Features a minimalist design with subtle gold edges.",
        "price": 749,
        "category": "Home Décor",
        "dimensions": "12cm x 8cm",
        "materials": "Crystal epoxy resin, gold leaf edges",
        "images": [
            "https://images.unsplash.com/photo-1596162954151-cdcb4c0f70a8?w=500",
            "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?w=500",
        ],
        "is_featured": False,
        "is_new": False,
    },
    {
        "name": "Rose Gold Earrings",
        "description": "Delicate rose gold themed resin earrings with embedded rose petals. Lightweight and comfortable for all-day wear.",
        "price": 449,
        "category": "Jewelry",
        "dimensions": "2.5cm drop",
        "materials": "Resin, dried rose petals, rose gold hooks",
        "images": [
            "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=500",
            "https://images.unsplash.com/photo-1588444837495-c6cfeb53f32d?w=500",
        ],
        "is_featured": True,
        "is_new": True,
    },
    {
        "name": "Marble Effect Cheese Board",
        "description": "Luxurious cheese board with stunning marble effect created using resin art techniques. Food-safe coating makes it perfect for entertaining.",
        "price": 1899,
        "category": "Kitchen",
        "dimensions": "35cm x 20cm",
        "materials": "Wood base, food-safe epoxy resin, marble pigments",
        "images": [
            "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500",
            "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=500",
        ],
        "is_featured": False,
        "is_new": False,
    },
    {
        "name": "Northern Lights Clock",
        "description": "Mesmerizing wall clock featuring aurora borealis design. The swirling greens and blues glow subtly in low light for a magical effect.",
        "price": 1599,
        "category": "Home Décor",
        "dimensions": "25cm diameter",
        "materials": "Epoxy resin, glow-in-dark pigments, clock mechanism",
        "images": [
            "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=500",
            "https://images.unsplash.com/photo-1507646227500-4d389b0012be?w=500",
            "https://images.unsplash.com/photo-1531685250784-7569952593d2?w=500",
        ],
        "is_featured": True,
        "is_new": False,
    },
    {
        "name": "Butterfly Wing Keychain",
        "description": "Delicate keychain featuring preserved butterfly wing pattern in crystal-clear resin. A unique accessory that celebrates nature's beauty.",
        "price": 299,
        "category": "Accessories",
        "dimensions": "5cm x 3cm",
        "materials": "UV resin, butterfly pattern film, metal keyring",
        "images": ["https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500"],
        "is_featured": False,
        "is_new": True,
    },
    {
        "name": "Geode Crystal Table",
        "description": "Stunning coffee table with geode crystal design. The centerpiece features deep purple amethyst colors with gold veining. A true statement piece.",
        "price": 8999,
        "category": "Furniture",
        "dimensions": "60cm x 40cm x 45cm",
        "materials": "Wood frame, epoxy resin, amethyst pigments, gold powder",
        "images": [
            "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=500",
            "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500",
            "https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=500",
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=500",
        ],
        "is_featured": True,
        "is_new": False,
    },
]

# Site settings
site_settings = {
    "type": "site_settings",
    "whatsapp": "919876543210",
    "instagram": "kalyani_resin_arts",
    "email": "hello@kalyaniresinarts.com",
    "address": "Hyderabad, Telangana, India",
    "about_text": "Welcome to Kalyani Resin Arts! We create beautiful handcrafted resin art pieces with love and creativity. Each piece is unique and made with premium quality materials.",
}

# Carousel slides
carousel_data = {
    "type": "carousel",
    "slides": [
        {
            "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=1200",
            "title": "Welcome to Kalyani Resin Arts",
            "subtitle": "Handcrafted with Love & Creativity",
        },
        {
            "image": "https://images.unsplash.com/photo-1616627577385-5c0c4dab4a3d?w=1200",
            "title": "Unique Resin Creations",
            "subtitle": "Each Piece Tells a Story",
        },
        {
            "image": "https://images.unsplash.com/photo-1596162954151-cdcb4c0f70a8?w=1200",
            "title": "Premium Quality Materials",
            "subtitle": "Crafted to Perfection",
        },
    ],
}


async def seed_database():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client.get_default_database()

    # Clear existing data
    print("Clearing existing data...")
    await db.products.delete_many({})
    await db.settings.delete_many({})

    # Insert products
    print("Inserting products...")
    for product in products:
        product["created_at"] = datetime.utcnow()
        product["updated_at"] = datetime.utcnow()

    result = await db.products.insert_many(products)
    print(f"Inserted {len(result.inserted_ids)} products")

    # Insert settings
    print("Inserting site settings...")
    await db.settings.insert_one(site_settings)

    # Insert carousel
    print("Inserting carousel data...")
    await db.settings.insert_one(carousel_data)

    print("\n✅ Database seeded successfully!")
    print(f"   - {len(products)} products added")
    print("   - Site settings configured")
    print("   - Carousel slides added")
    print("\nYou can now view the products at http://localhost:3000")

    client.close()


if __name__ == "__main__":
    asyncio.run(seed_database())
