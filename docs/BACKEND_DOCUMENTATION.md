# 🔧 Backend Documentation - Kalyani Resin Arts

## Table of Contents

1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Environment Configuration](#environment-configuration)
6. [Understanding FastAPI](#understanding-fastapi)
7. [Database Setup (MongoDB)](#database-setup-mongodb)
8. [API Routes Explained](#api-routes-explained)
9. [Models (Data Structures)](#models-data-structures)
10. [Authentication](#authentication)
11. [Image Upload (Cloudinary)](#image-upload-cloudinary)
12. [API Reference](#api-reference)
13. [Deployment](#deployment)
14. [Troubleshooting](#troubleshooting)

---

## Introduction

Welcome! 👋 This documentation explains the backend of Kalyani Resin Arts project in a beginner-friendly way.

**What is a Backend?**

The backend is the "behind-the-scenes" part of our application. It:

- Stores data in a database
- Handles business logic
- Provides API endpoints for the frontend to consume
- Manages authentication and security

**What does our Backend do?**

- ✅ Stores products, reviews, and settings in MongoDB
- ✅ Provides REST API endpoints
- ✅ Handles admin authentication
- ✅ Manages image uploads to Cloudinary
- ✅ Serves data to the frontend

---

## Technology Stack

| Technology     | Version | Purpose                         |
| -------------- | ------- | ------------------------------- |
| **Python**     | 3.9+    | Programming language            |
| **FastAPI**    | 0.104.1 | Web framework for building APIs |
| **Uvicorn**    | 0.24.0  | ASGI server (runs our app)      |
| **Motor**      | 3.3.2   | Async MongoDB driver            |
| **Pydantic**   | 2.5.2   | Data validation                 |
| **Cloudinary** | 1.36.0  | Cloud image hosting             |

### What is FastAPI?

FastAPI is a modern Python web framework for building APIs. It's:

- **Fast** - One of the fastest Python frameworks
- **Easy** - Simple to write and understand
- **Automatic docs** - Generates API documentation automatically
- **Type-safe** - Uses Python type hints for validation

### What is MongoDB?

MongoDB is a NoSQL database that stores data in JSON-like documents. Unlike SQL databases (tables and rows), MongoDB uses collections and documents.

**Example document:**

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "Ocean Wave Coaster",
  "price": 899,
  "category": "Coasters"
}
```

---

## Project Structure

```
backend/
├── requirements.txt      # Python dependencies
├── seed_data.py         # Script to add sample data
├── vercel.json          # Vercel deployment config
│
└── app/                 # Main application code
    ├── __init__.py      # Makes this a Python package
    ├── main.py          # Application entry point
    │
    ├── auth/            # Authentication logic
    │   ├── __init__.py
    │   └── basic_auth.py    # HTTP Basic Auth implementation
    │
    ├── config/          # Configuration files
    │   ├── __init__.py
    │   ├── database.py      # MongoDB connection
    │   └── settings.py      # App settings
    │
    ├── models/          # Data models (schemas)
    │   ├── __init__.py
    │   ├── product.py       # Product model
    │   ├── review.py        # Review model
    │   └── settings.py      # Settings model
    │
    └── routes/          # API endpoints
        ├── __init__.py
        ├── auth.py          # Login endpoints
        ├── products.py      # Product CRUD endpoints
        ├── reviews.py       # Review CRUD endpoints
        ├── settings.py      # Settings endpoints
        └── upload.py        # Image upload endpoint
```

### Understanding the Structure

**Think of it like a restaurant:**

- `main.py` = The front desk (receives all requests)
- `routes/` = Different service counters (products, reviews, etc.)
- `models/` = The menu (defines what data looks like)
- `config/` = Kitchen settings (database, environment)
- `auth/` = Security guard (checks who can enter)

---

## Getting Started

### Prerequisites

1. **Python 3.9 or higher**
   - Download from: https://python.org/
   - Verify: `python --version`

2. **pip** (Python package installer)
   - Usually comes with Python
   - Verify: `pip --version`

### Installation Steps

```bash
# Step 1: Navigate to backend folder
cd backend

# Step 2: Create a virtual environment (recommended)
python -m venv venv

# Step 3: Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Run the development server
uvicorn app.main:app --reload
```

After running the last command, you'll see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Connected to MongoDB
```

### What is `uvicorn app.main:app --reload`?

Let's break it down:

- `uvicorn` - The server program
- `app.main` - Path to our main.py file (app/main.py)
- `:app` - The FastAPI instance variable name
- `--reload` - Auto-restart when code changes

### API Documentation

FastAPI automatically generates interactive API docs!

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Try them out! You can test endpoints directly from the browser.

---

## Environment Configuration

### Settings File (`config/settings.py`)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MongoDB connection string
    mongodb_url: str = "your-mongodb-url"

    # Admin login credentials
    admin_username: str = "admin"
    admin_password: str = "admin123"

    # Debug mode
    debug: bool = True

    # Allowed frontend origins (for CORS)
    allowed_origins: str = "http://localhost:5173,http://localhost:3000"

    # Cloudinary settings (for image upload)
    cloudinary_cloud_name: str = ""
    cloudinary_api_key: str = ""
    cloudinary_api_secret: str = ""

    class Config:
        env_file = ".env"  # Load from .env file
```

### Creating a `.env` File

Create a `.env` file in the `backend/` folder:

```env
# MongoDB
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/database

# Admin Credentials (change these!)
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-secure-password

# Debug Mode
DEBUG=true

# Allowed Origins (comma-separated)
ALLOWED_ORIGINS=http://localhost:5173,https://your-domain.com

# Cloudinary (get from cloudinary.com)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### Security Warning ⚠️

**NEVER commit `.env` files to git!**

Add to `.gitignore`:

```
.env
*.env
```

---

## Understanding FastAPI

### Basic FastAPI Application

Here's our `main.py` explained:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Import our database functions
from app.config.database import connect_to_mongo, close_mongo_connection

# Import our route modules
from app.routes import products, settings, auth, upload, reviews


# Lifespan: What happens when app starts and stops
@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP: Runs when server starts
    await connect_to_mongo()  # Connect to database
    yield  # App is now running
    # SHUTDOWN: Runs when server stops
    await close_mongo_connection()  # Disconnect from database


# Create the FastAPI application
app = FastAPI(
    title="Kalyani Resin Arts API",
    description="Backend API for the e-commerce showcase",
    version="1.0.0",
    lifespan=lifespan,
)


# CORS: Allow frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Register routes (plug in our endpoints)
app.include_router(products.router, prefix="/api")
app.include_router(settings.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(reviews.router, prefix="/api")


# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Kalyani Resin Arts API",
        "docs": "/docs"
    }


# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
```

### Key Concepts

#### 1. Decorators (`@app.get`, `@app.post`, etc.)

Decorators define what HTTP method and path trigger a function:

```python
@app.get("/products")      # GET request to /products
@app.post("/products")     # POST request to /products
@app.put("/products/{id}") # PUT request to /products/123
@app.delete("/products/{id}") # DELETE request to /products/123
```

#### 2. Path Parameters

Values in the URL:

```python
@app.get("/products/{product_id}")
async def get_product(product_id: str):
    # product_id = "123" if URL is /products/123
    return {"id": product_id}
```

#### 3. Request Body

Data sent in POST/PUT requests:

```python
@app.post("/products")
async def create_product(product: ProductCreate):
    # product contains the JSON body
    return product
```

#### 4. Query Parameters

Optional filters in URL:

```python
@app.get("/products")
async def get_products(category: str = None, limit: int = 10):
    # URL: /products?category=Coasters&limit=5
    return {"category": category, "limit": limit}
```

#### 5. Async/Await

Python's way of handling non-blocking operations:

```python
# Without async (blocks while waiting)
def get_data():
    data = database.find()  # Waits here
    return data

# With async (doesn't block)
async def get_data():
    data = await database.find()  # Continues while waiting
    return data
```

---

## Database Setup (MongoDB)

### Connection File (`config/database.py`)

```python
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

# Global variables for connection
client = None
db = None


async def connect_to_mongo():
    """Connect to MongoDB when app starts"""
    global client, db

    # Create connection to MongoDB
    client = AsyncIOMotorClient(settings.mongodb_url)

    # Get the default database from connection string
    db = client.get_default_database()

    print("Connected to MongoDB")


async def close_mongo_connection():
    """Close connection when app stops"""
    global client
    if client:
        client.close()
        print("MongoDB connection closed")


def get_database():
    """Get database instance for use in routes"""
    return db
```

### Understanding MongoDB Operations

#### Collections

Think of collections like tables in SQL:

- `products` - Stores all products
- `reviews` - Stores customer reviews
- `settings` - Stores site configuration

#### Common Operations

```python
# Get database reference
db = get_database()

# INSERT - Add new document
result = await db.products.insert_one({
    "name": "Ocean Coaster",
    "price": 899
})

# FIND ALL - Get all documents
products = await db.products.find().to_list(100)

# FIND ONE - Get single document
product = await db.products.find_one({"_id": ObjectId("...")})

# UPDATE - Modify document
await db.products.update_one(
    {"_id": ObjectId("...")},  # Filter
    {"$set": {"price": 999}}   # Update
)

# DELETE - Remove document
await db.products.delete_one({"_id": ObjectId("...")})
```

### MongoDB Document Structure

#### Product Document

```json
{
  "_id": "ObjectId",
  "name": "Ocean Wave Coaster Set",
  "description": "Beautiful handcrafted resin coasters...",
  "price": 899,
  "category": "Coasters",
  "dimensions": "10cm x 10cm (Set of 4)",
  "materials": "Epoxy resin, blue pigments...",
  "images": [
    "https://cloudinary.com/image1.jpg",
    "https://cloudinary.com/image2.jpg"
  ],
  "is_featured": true,
  "is_new": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

---

## API Routes Explained

### Products Route (`routes/products.py`)

This file handles all product-related operations.

```python
from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from datetime import datetime
from app.config.database import get_database
from app.models.product import ProductCreate, ProductUpdate
from app.auth.basic_auth import verify_credentials

# Create a router (group of endpoints)
router = APIRouter(prefix="/products", tags=["Products"])


# Helper function to convert MongoDB document
def serialize_product(product) -> dict:
    """Convert MongoDB document to JSON-friendly format"""
    if product:
        product["_id"] = str(product["_id"])  # ObjectId → string
    return product


# GET /api/products - List all products
@router.get("")
async def get_all_products():
    """Get all products (PUBLIC - anyone can access)"""
    db = get_database()

    # Find all products, sorted by newest first
    products = await db.products.find().sort("created_at", -1).to_list(100)

    # Convert ObjectIds to strings
    return [serialize_product(p) for p in products]


# GET /api/products/featured - Get featured products
@router.get("/featured")
async def get_featured_products():
    """Get products marked as featured"""
    db = get_database()

    # Find only products where is_featured = True
    products = await db.products.find({"is_featured": True}).to_list(10)

    return [serialize_product(p) for p in products]


# GET /api/products/{id} - Get single product
@router.get("/{product_id}")
async def get_product(product_id: str):
    """Get one product by its ID"""
    db = get_database()

    # Validate the ID format
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    # Find the product
    product = await db.products.find_one({"_id": ObjectId(product_id)})

    # 404 if not found
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return serialize_product(product)


# POST /api/products - Create product (ADMIN ONLY)
@router.post("", status_code=201)
async def create_product(
    product: ProductCreate,
    username: str = Depends(verify_credentials)  # Requires login!
):
    """Create a new product"""
    db = get_database()

    # Convert Pydantic model to dictionary
    product_dict = product.model_dump()

    # Add timestamps
    product_dict["created_at"] = datetime.utcnow()
    product_dict["updated_at"] = datetime.utcnow()

    # Insert into database
    result = await db.products.insert_one(product_dict)

    # Add the generated ID to response
    product_dict["_id"] = str(result.inserted_id)

    return product_dict


# PUT /api/products/{id} - Update product (ADMIN ONLY)
@router.put("/{product_id}")
async def update_product(
    product_id: str,
    product: ProductUpdate,
    username: str = Depends(verify_credentials)
):
    """Update an existing product"""
    db = get_database()

    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    # Only include fields that were actually sent
    update_data = {k: v for k, v in product.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()

    # Update in database
    result = await db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    # Return updated product
    updated = await db.products.find_one({"_id": ObjectId(product_id)})
    return serialize_product(updated)


# DELETE /api/products/{id} - Delete product (ADMIN ONLY)
@router.delete("/{product_id}", status_code=204)
async def delete_product(
    product_id: str,
    username: str = Depends(verify_credentials)
):
    """Delete a product"""
    db = get_database()

    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    result = await db.products.delete_one({"_id": ObjectId(product_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return None  # 204 No Content
```

### Key Concepts Explained

#### 1. `Depends(verify_credentials)`

This is **Dependency Injection**. It means:

- Before running this function, run `verify_credentials` first
- If credentials are invalid, return 401 error
- If valid, continue with the request

```python
# This endpoint requires admin login
@router.post("")
async def create_product(
    product: ProductCreate,
    username: str = Depends(verify_credentials)  # Runs auth check first
):
    # Only reaches here if authenticated
    ...
```

#### 2. `HTTPException`

Used to return error responses:

```python
# Returns: {"detail": "Product not found"} with 404 status
raise HTTPException(status_code=404, detail="Product not found")

# Returns: {"detail": "Invalid ID"} with 400 status
raise HTTPException(status_code=400, detail="Invalid ID")
```

#### 3. `status_code=201`

Sets the HTTP status code for the response:

- `200` = OK (default)
- `201` = Created (after POST)
- `204` = No Content (after DELETE)
- `400` = Bad Request
- `401` = Unauthorized
- `404` = Not Found

---

## Models (Data Structures)

### What are Models?

Models define the **shape** of our data. They:

- Validate incoming data
- Define required vs optional fields
- Set default values
- Generate documentation

### Product Model (`models/product.py`)

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# Base model with common fields
class ProductBase(BaseModel):
    name: str                           # Required string
    description: Optional[str] = None   # Optional string
    price: float                        # Required number
    category: Optional[str] = None      # Optional string
    dimensions: Optional[str] = None    # Optional string
    materials: Optional[str] = None     # Optional string
    images: List[str] = []              # List of strings, default empty
    is_featured: bool = False           # Boolean, default False
    is_new: bool = False                # Boolean, default False


# For creating new products (inherits all from ProductBase)
class ProductCreate(ProductBase):
    pass


# For updating products (all fields optional)
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


# For reading products from database
class ProductResponse(ProductBase):
    id: str = Field(alias="_id")         # MongoDB uses _id
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        populate_by_name = True  # Accept both "id" and "_id"
```

### Understanding Pydantic

#### Type Hints

```python
name: str           # Must be a string
price: float        # Must be a number
is_featured: bool   # Must be True or False
images: List[str]   # Must be a list of strings
```

#### Optional Fields

```python
# Required - must be provided
name: str

# Optional - can be None or not provided
description: Optional[str] = None
```

#### Default Values

```python
is_featured: bool = False  # If not provided, defaults to False
images: List[str] = []     # If not provided, defaults to empty list
```

#### Validation Example

If someone sends this JSON:

```json
{
  "name": 123,
  "price": "not a number"
}
```

Pydantic will return an error:

```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "str type expected",
      "type": "type_error.str"
    },
    {
      "loc": ["body", "price"],
      "msg": "value is not a valid float",
      "type": "type_error.float"
    }
  ]
}
```

### Review Model (`models/review.py`)

```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ReviewBase(BaseModel):
    customer_name: str = Field(..., min_length=1, max_length=100)
    customer_image: Optional[str] = None
    rating: int = Field(..., ge=1, le=5)  # Between 1-5
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
```

#### Field Validations

```python
# String length validation
customer_name: str = Field(..., min_length=1, max_length=100)

# Number range validation
rating: int = Field(..., ge=1, le=5)  # ge = greater or equal, le = less or equal
```

### Settings Model (`models/settings.py`)

```python
from pydantic import BaseModel
from typing import Optional, List


class CarouselSlide(BaseModel):
    image: str                     # Image URL
    title: Optional[str] = None    # Optional title
    subtitle: Optional[str] = None # Optional subtitle


class FeatureCard(BaseModel):
    icon: str = "✨"    # Emoji or icon
    title: str          # Card title
    description: str    # Card description


class SiteSettings(BaseModel):
    whatsapp: Optional[str] = None
    instagram: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    about_text: Optional[str] = None
    hero_title: Optional[str] = None
    hero_subtitle: Optional[str] = None
    footer_text: Optional[str] = None
```

---

## Authentication

### How Our Auth Works

We use **HTTP Basic Authentication**:

1. Client sends username:password encoded in Base64
2. Server decodes and verifies credentials
3. If valid, allows the request
4. If invalid, returns 401 Unauthorized

### Auth Implementation (`auth/basic_auth.py`)

```python
import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.config.settings import settings

# Create HTTP Basic security scheme
security = HTTPBasic()


def verify_credentials(
    credentials: HTTPBasicCredentials = Depends(security)
):
    """
    Verify admin credentials.
    This runs BEFORE protected endpoints.
    """

    # Use secrets.compare_digest for timing-attack safe comparison
    correct_username = secrets.compare_digest(
        credentials.username.encode("utf8"),
        settings.admin_username.encode("utf8")
    )
    correct_password = secrets.compare_digest(
        credentials.password.encode("utf8"),
        settings.admin_password.encode("utf8")
    )

    # If either is wrong, deny access
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    # Return username for logging/tracking
    return credentials.username
```

### Why `secrets.compare_digest()`?

Normal string comparison (`==`) can be vulnerable to timing attacks:

- An attacker can measure how long comparison takes
- More matching characters = longer time
- They can guess the password character by character

`compare_digest()` takes constant time regardless of match length.

### Using Auth in Routes

```python
from app.auth.basic_auth import verify_credentials
from fastapi import Depends

# PUBLIC endpoint - no auth needed
@router.get("/products")
async def get_products():
    return products

# PROTECTED endpoint - requires admin login
@router.post("/products")
async def create_product(
    product: ProductCreate,
    username: str = Depends(verify_credentials)  # <- This requires auth
):
    return created_product
```

### Auth Routes (`routes/auth.py`)

```python
from fastapi import APIRouter, Depends
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
async def login(username: str = Depends(verify_credentials)):
    """
    Login endpoint.
    If credentials are valid, verify_credentials passes.
    If invalid, it raises 401 before we reach here.
    """
    return {"message": "Login successful", "username": username}


@router.get("/verify")
async def verify_token(username: str = Depends(verify_credentials)):
    """
    Verify if credentials are still valid.
    Frontend calls this to check if user is still logged in.
    """
    return {"valid": True, "username": username}
```

---

## Image Upload (Cloudinary)

### What is Cloudinary?

Cloudinary is a cloud service for storing and managing images. Benefits:

- Stores images on their servers (not ours)
- Automatic image optimization
- Image transformations (resize, crop, etc.)
- CDN for fast loading worldwide

### Upload Implementation (`routes/upload.py`)

```python
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import cloudinary
import cloudinary.uploader
from app.config.settings import settings
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/upload", tags=["Upload"])

# Configure Cloudinary with our credentials
cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret,
)


@router.post("")
async def upload_image(
    file: UploadFile = File(...),  # The uploaded file
    username: str = Depends(verify_credentials)  # Admin only
):
    """Upload an image to Cloudinary"""

    # Step 1: Validate file type
    allowed_types = ["image/jpeg", "image/png", "image/webp", "image/gif"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Allowed: JPEG, PNG, WebP, GIF"
        )

    # Step 2: Read file contents
    contents = await file.read()

    # Step 3: Validate file size (max 5MB)
    if len(contents) > 5 * 1024 * 1024:  # 5MB in bytes
        raise HTTPException(
            status_code=400,
            detail="File too large. Maximum size is 5MB"
        )

    try:
        # Step 4: Upload to Cloudinary
        result = cloudinary.uploader.upload(
            contents,
            folder="kalyani_resin_arts",  # Organize in folder
            resource_type="image",
            transformation=[
                {"width": 1200, "height": 1200, "crop": "limit"},
                {"quality": "auto:good"}
            ]
        )

        # Step 5: Return image URL and info
        return {
            "url": result["secure_url"],      # HTTPS URL to image
            "public_id": result["public_id"],  # Unique ID for deletion
            "width": result.get("width"),
            "height": result.get("height")
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to upload image: {str(e)}"
        )


@router.delete("/{public_id:path}")
async def delete_image(
    public_id: str,
    username: str = Depends(verify_credentials)
):
    """Delete an image from Cloudinary"""
    try:
        result = cloudinary.uploader.destroy(public_id)

        if result.get("result") == "ok":
            return {"message": "Image deleted successfully"}
        else:
            raise HTTPException(status_code=400, detail="Failed to delete image")

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to delete image: {str(e)}"
        )
```

### Getting Cloudinary Credentials

1. Sign up at https://cloudinary.com (free tier available)
2. Go to Dashboard
3. Copy your Cloud Name, API Key, and API Secret
4. Add them to your `.env` file

---

## API Reference

### Quick Reference Table

| Method       | Endpoint                  | Description           | Auth Required |
| ------------ | ------------------------- | --------------------- | ------------- |
| GET          | `/`                       | Welcome message       | No            |
| GET          | `/api/health`             | Health check          | No            |
| **Products** |
| GET          | `/api/products`           | Get all products      | No            |
| GET          | `/api/products/featured`  | Get featured products | No            |
| GET          | `/api/products/{id}`      | Get single product    | No            |
| POST         | `/api/products`           | Create product        | Yes           |
| PUT          | `/api/products/{id}`      | Update product        | Yes           |
| DELETE       | `/api/products/{id}`      | Delete product        | Yes           |
| **Reviews**  |
| GET          | `/api/reviews`            | Get all reviews       | No            |
| GET          | `/api/reviews/featured`   | Get featured reviews  | No            |
| GET          | `/api/reviews/{id}`       | Get single review     | No            |
| POST         | `/api/reviews`            | Create review         | Yes           |
| PUT          | `/api/reviews/{id}`       | Update review         | Yes           |
| DELETE       | `/api/reviews/{id}`       | Delete review         | Yes           |
| **Settings** |
| GET          | `/api/settings`           | Get site settings     | No            |
| PUT          | `/api/settings`           | Update settings       | Yes           |
| GET          | `/api/settings/carousel`  | Get carousel slides   | No            |
| PUT          | `/api/settings/carousel`  | Update carousel       | Yes           |
| GET          | `/api/settings/features`  | Get feature cards     | No            |
| PUT          | `/api/settings/features`  | Update features       | Yes           |
| **Auth**     |
| POST         | `/api/auth/login`         | Admin login           | Yes           |
| GET          | `/api/auth/verify`        | Verify credentials    | Yes           |
| **Upload**   |
| POST         | `/api/upload`             | Upload image          | Yes           |
| DELETE       | `/api/upload/{public_id}` | Delete image          | Yes           |

### Detailed Endpoint Examples

#### Create Product

**Request:**

```http
POST /api/products
Authorization: Basic YWRtaW46YWRtaW4xMjM=
Content-Type: application/json

{
  "name": "Ocean Wave Coaster Set",
  "description": "Beautiful handcrafted resin coasters",
  "price": 899,
  "category": "Coasters",
  "dimensions": "10cm x 10cm",
  "materials": "Epoxy resin, blue pigments",
  "images": ["https://example.com/image1.jpg"],
  "is_featured": true,
  "is_new": false
}
```

**Response (201 Created):**

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "Ocean Wave Coaster Set",
  "description": "Beautiful handcrafted resin coasters",
  "price": 899,
  "category": "Coasters",
  "dimensions": "10cm x 10cm",
  "materials": "Epoxy resin, blue pigments",
  "images": ["https://example.com/image1.jpg"],
  "is_featured": true,
  "is_new": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

#### Error Response Example

**Request with invalid data:**

```http
POST /api/products
Authorization: Basic YWRtaW46YWRtaW4xMjM=

{
  "description": "Missing required fields"
}
```

**Response (422 Unprocessable Entity):**

```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "price"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## Deployment

### Vercel Deployment

Our project is configured for Vercel serverless deployment.

**Backend `vercel.json`:**

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/main.py"
    }
  ]
}
```

### Deployment Steps

1. **Push to GitHub**

2. **Connect to Vercel**
   - Go to vercel.com
   - Import your GitHub repository
   - Select the `backend` folder as root

3. **Set Environment Variables**

   In Vercel dashboard, add:
   - `MONGODB_URL`
   - `ADMIN_USERNAME`
   - `ADMIN_PASSWORD`
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`
   - `ALLOWED_ORIGINS` (your frontend URL)

4. **Deploy!**

### Seed Database

To add sample products to a new database:

```bash
cd backend
python seed_data.py
```

This script adds dummy products for testing.

---

## Troubleshooting

### Common Issues

#### 1. "Module not found" Error

**Solution:** Make sure you're in a virtual environment and installed dependencies:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### 2. MongoDB Connection Failed

**Check:**

- Is your MongoDB URL correct in `.env`?
- Is your IP whitelisted in MongoDB Atlas?
- Is the database user credentials correct?

**MongoDB Atlas IP Whitelist:**

1. Go to MongoDB Atlas dashboard
2. Network Access → Add IP Address
3. Add `0.0.0.0/0` for any IP (development only!)

#### 3. CORS Errors

**Error:** "Access to XMLHttpRequest at ... has been blocked by CORS policy"

**Solution:** Add your frontend URL to `ALLOWED_ORIGINS`:

```env
ALLOWED_ORIGINS=http://localhost:5173,https://your-frontend.com
```

#### 4. 401 Unauthorized

**Check:**

- Is Authorization header sent correctly?
- Are credentials correct in `.env`?
- Is the token Base64 encoded properly?

**Debug in terminal:**

```python
import base64
credentials = base64.b64encode(b"admin:admin123").decode()
print(credentials)  # YWRtaW46YWRtaW4xMjM=
```

#### 5. 422 Validation Error

**Meaning:** The request data doesn't match the expected format.

**Solution:** Check the response body for details:

```json
{
  "detail": [
    {
      "loc": ["body", "price"],
      "msg": "value is not a valid float",
      "type": "type_error.float"
    }
  ]
}
```

This tells you exactly which field is wrong.

#### 6. Image Upload Failing

**Check:**

- Are Cloudinary credentials set?
- Is file type allowed (JPEG, PNG, WebP, GIF)?
- Is file size under 5MB?
- Is admin authenticated?

### Debugging Tips

1. **Check the Logs**

   ```bash
   uvicorn app.main:app --reload --log-level debug
   ```

2. **Use Print Statements**

   ```python
   @router.post("/products")
   async def create_product(product: ProductCreate):
       print(f"Received product: {product}")
       # ... rest of code
   ```

3. **Test with Swagger UI**
   - Go to http://localhost:8000/docs
   - Click "Authorize" and enter credentials
   - Try endpoints directly

4. **Use Postman or curl**

   ```bash
   curl -X GET http://localhost:8000/api/products

   curl -X POST http://localhost:8000/api/auth/login \
     -H "Authorization: Basic YWRtaW46YWRtaW4xMjM="
   ```

---

## Quick Reference

### Files to Edit for...

| Task                     | File                                              |
| ------------------------ | ------------------------------------------------- |
| Add new API endpoint     | Create route in `routes/` + register in `main.py` |
| Add new data model       | Create model in `models/`                         |
| Change database settings | `config/database.py`                              |
| Change app settings      | `config/settings.py` or `.env`                    |
| Modify authentication    | `auth/basic_auth.py`                              |

### Useful Commands

```bash
# Start dev server
uvicorn app.main:app --reload

# Start with specific port
uvicorn app.main:app --reload --port 8001

# Seed database
python seed_data.py

# Check Python version
python --version

# Install single package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Motor (Async MongoDB)](https://motor.readthedocs.io/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)

---

**Happy Coding! 🚀**

If you have questions, check the FastAPI docs at http://localhost:8000/docs or reach out to the team.
