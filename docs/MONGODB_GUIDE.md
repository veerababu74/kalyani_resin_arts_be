# 🍃 MongoDB Complete Guide - Kalyani Resin Arts

## Table of Contents

1. [What is MongoDB?](#what-is-mongodb)
2. [MongoDB vs SQL Databases](#mongodb-vs-sql-databases)
3. [Key Concepts](#key-concepts)
4. [MongoDB Atlas Setup](#mongodb-atlas-setup)
5. [How Our Project Uses MongoDB](#how-our-project-uses-mongodb)
6. [Collections in Our Project](#collections-in-our-project)
7. [How Collections Are Created](#how-collections-are-created)
8. [CRUD Operations Explained](#crud-operations-explained)
9. [Query Examples](#query-examples)
10. [Understanding ObjectId](#understanding-objectid)
11. [Connection String Explained](#connection-string-explained)
12. [Viewing Your Data](#viewing-your-data)
13. [Common Issues](#common-issues)

---

## What is MongoDB?

### Simple Explanation

Imagine MongoDB as a **filing cabinet**:

- The **database** = The entire filing cabinet
- **Collections** = Different drawers in the cabinet (Products drawer, Reviews drawer)
- **Documents** = Individual papers/files in each drawer

### Technical Explanation

MongoDB is a **NoSQL database** that stores data in **JSON-like documents**. Instead of tables with rows and columns (like Excel), it uses flexible documents that can have different structures.

### Example Document

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "Ocean Wave Coaster",
  "price": 899,
  "category": "Coasters",
  "images": ["image1.jpg", "image2.jpg"],
  "is_featured": true
}
```

**This is ONE document** - like a single product card with all its information.

---

## MongoDB vs SQL Databases

### Visual Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│                        SQL (MySQL, PostgreSQL)                  │
├─────────────────────────────────────────────────────────────────┤
│  Database: kalyani_resin_arts                                   │
│  └── Table: products                                            │
│      ├── id (INT)                                               │
│      ├── name (VARCHAR)                                         │
│      ├── price (DECIMAL)                                        │
│      └── category (VARCHAR)                                     │
│                                                                 │
│  Data looks like:                                               │
│  ┌────┬───────────────────┬───────┬───────────┐                 │
│  │ id │ name              │ price │ category  │                 │
│  ├────┼───────────────────┼───────┼───────────┤                 │
│  │ 1  │ Ocean Coaster     │ 899   │ Coasters  │                 │
│  │ 2  │ Galaxy Pendant    │ 599   │ Jewelry   │                 │
│  └────┴───────────────────┴───────┴───────────┘                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                        MongoDB (NoSQL)                          │
├─────────────────────────────────────────────────────────────────┤
│  Database: kalyani_resin_arts                                   │
│  └── Collection: products                                       │
│                                                                 │
│  Data looks like:                                               │
│  {                                                              │
│    "_id": "507f1f77bcf86cd799439011",                          │
│    "name": "Ocean Coaster",                                     │
│    "price": 899,                                                │
│    "category": "Coasters",                                      │
│    "images": ["img1.jpg", "img2.jpg"]  ← Can store arrays!     │
│  }                                                              │
│  {                                                              │
│    "_id": "507f1f77bcf86cd799439012",                          │
│    "name": "Galaxy Pendant",                                    │
│    "price": 599,                                                │
│    "category": "Jewelry"                                        │
│  }                                                              │
└─────────────────────────────────────────────────────────────────┘
```

### Terminology Comparison

| SQL Term    | MongoDB Term | Example                     |
| ----------- | ------------ | --------------------------- |
| Database    | Database     | `kalyani_resin_arts`        |
| Table       | Collection   | `products`, `reviews`       |
| Row         | Document     | One product's data          |
| Column      | Field        | `name`, `price`, `category` |
| Primary Key | `_id`        | Auto-generated unique ID    |

### Key Differences

| Feature       | SQL                               | MongoDB                           |
| ------------- | --------------------------------- | --------------------------------- |
| Schema        | Fixed (must define columns first) | Flexible (can add fields anytime) |
| Data Format   | Rows and columns                  | JSON documents                    |
| Arrays        | Need separate table               | Store directly in document        |
| Relationships | Foreign keys, JOINs               | Embed or reference                |

---

## Key Concepts

### 1. Database

A **database** is a container for all your data. Our project uses one database called `kalyani_resin_arts`.

```
kalyani_resin_arts (Database)
├── products (Collection)
├── reviews (Collection)
└── settings (Collection)
```

### 2. Collection

A **collection** is a group of related documents. Think of it as a folder for similar items.

```
products collection:
├── Document 1 (Ocean Coaster)
├── Document 2 (Galaxy Pendant)
├── Document 3 (Floral Bookmark)
└── ... more products
```

### 3. Document

A **document** is a single record. It's stored in **BSON format** (Binary JSON).

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "Ocean Wave Coaster Set",
  "description": "Beautiful handcrafted resin coasters",
  "price": 899,
  "category": "Coasters",
  "images": [
    "https://cloudinary.com/image1.jpg",
    "https://cloudinary.com/image2.jpg"
  ],
  "is_featured": true,
  "is_new": false,
  "created_at": "2024-01-15T10:30:00Z"
}
```

### 4. Field

A **field** is a key-value pair in a document. Like `"name": "Ocean Coaster"`.

### 5. \_id (Primary Key)

Every document has a unique `_id` field. MongoDB auto-generates this if you don't provide one.

```json
"_id": "507f1f77bcf86cd799439011"
```

This is called an **ObjectId** - a 12-byte unique identifier.

---

## MongoDB Atlas Setup

### What is MongoDB Atlas?

MongoDB Atlas is **MongoDB in the cloud**. Instead of installing MongoDB on your computer, you use their servers. It's:

- Free (for small projects)
- Easy to set up
- Accessible from anywhere

### Step-by-Step Setup

#### Step 1: Create Account

1. Go to https://www.mongodb.com/cloud/atlas
2. Click "Try Free"
3. Sign up with email or Google

#### Step 2: Create a Cluster

1. After login, click "Build a Database"
2. Choose **FREE tier** (M0 Sandbox)
3. Select a cloud provider (AWS, Google Cloud, or Azure)
4. Choose a region close to you
5. Click "Create Cluster"

```
┌─────────────────────────────────────────────────────────────────┐
│                     Create a Cluster                            │
├─────────────────────────────────────────────────────────────────┤
│  ○ Serverless (pay per operation)                               │
│  ○ Dedicated (for production)                                   │
│  ● Shared (FREE)  ← Choose this!                                │
│                                                                 │
│  Provider: AWS                                                  │
│  Region: Mumbai (ap-south-1)                                    │
│  Cluster Name: kalyaniresinarts                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Step 3: Create Database User

1. Go to "Database Access" (left sidebar)
2. Click "Add New Database User"
3. Choose "Password" authentication
4. Enter username and password
5. Save these credentials! You'll need them.

```
Username: veera
Password: veera7474 (use a stronger password!)
```

#### Step 4: Allow Network Access

1. Go to "Network Access" (left sidebar)
2. Click "Add IP Address"
3. For development: Click "Allow Access from Anywhere" (0.0.0.0/0)
4. For production: Add specific IP addresses

```
⚠️ Security Note:
"Allow from Anywhere" is convenient for development but less secure.
For production, add only your server's IP address.
```

#### Step 5: Get Connection String

1. Go to "Database" (left sidebar)
2. Click "Connect" on your cluster
3. Choose "Connect your application"
4. Copy the connection string

```
mongodb+srv://veera:<password>@kalyaniresinarts.7mmmbo5.mongodb.net/?retryWrites=true&w=majority
```

5. Replace `<password>` with your actual password
6. Add database name before the `?`:

```
mongodb+srv://veera:veera7474@kalyaniresinarts.7mmmbo5.mongodb.net/kalyani_resin_arts?retryWrites=true&w=majority
                                                                    ↑
                                                         Add database name here!
```

---

## How Our Project Uses MongoDB

### Connection Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        Our Application                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 1. App starts
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    config/database.py                           │
│  - Connects to MongoDB using connection string                  │
│  - Stores database reference in 'db' variable                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 2. Uses Motor (async driver)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     MongoDB Atlas                               │
│  - Cloud-hosted database                                        │
│  - Stores all our data                                          │
└─────────────────────────────────────────────────────────────────┘
```

### Database Connection Code

**File: `backend/app/config/database.py`**

```python
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

# These will hold our connection
client = None  # MongoDB client (connection to MongoDB)
db = None      # Database reference (our specific database)


async def connect_to_mongo():
    """
    This function runs when the app STARTS.
    It creates a connection to MongoDB.
    """
    global client, db

    # Create connection using our connection string
    # settings.mongodb_url = "mongodb+srv://user:pass@cluster.../kalyani_resin_arts"
    client = AsyncIOMotorClient(settings.mongodb_url)

    # Get the database from the connection string
    # The database name is in the URL: .../kalyani_resin_arts?...
    db = client.get_default_database()

    print("Connected to MongoDB")


async def close_mongo_connection():
    """
    This function runs when the app STOPS.
    It closes the connection properly.
    """
    global client
    if client:
        client.close()
        print("MongoDB connection closed")


def get_database():
    """
    Returns the database reference.
    Routes use this to access collections.
    """
    return db
```

### How Routes Use the Database

```python
from app.config.database import get_database

@router.get("/products")
async def get_products():
    # Step 1: Get database reference
    db = get_database()

    # Step 2: Access 'products' collection and find all documents
    products = await db.products.find().to_list(100)

    # Step 3: Return the data
    return products
```

**Breaking down `db.products.find().to_list(100)`:**

```python
db              # Our database (kalyani_resin_arts)
.products       # The 'products' collection
.find()         # Find documents (like SELECT in SQL)
.to_list(100)   # Convert to list, max 100 items
```

---

## Collections in Our Project

Our project has **3 collections**:

### 1. Products Collection

Stores all product information.

```json
// Collection: products
// Example document:
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "Ocean Wave Coaster Set",
  "description": "Beautiful handcrafted resin coasters with ocean wave design.",
  "price": 899,
  "category": "Coasters",
  "dimensions": "10cm x 10cm (Set of 4)",
  "materials": "Epoxy resin, blue pigments, gold flakes",
  "images": [
    "https://res.cloudinary.com/xxx/image1.jpg",
    "https://res.cloudinary.com/xxx/image2.jpg"
  ],
  "is_featured": true,
  "is_new": false,
  "created_at": "2024-01-15T10:30:00.000Z",
  "updated_at": "2024-01-15T10:30:00.000Z"
}
```

**Fields explained:**

| Field         | Type     | Description                        |
| ------------- | -------- | ---------------------------------- |
| `_id`         | ObjectId | Unique identifier (auto-generated) |
| `name`        | String   | Product name                       |
| `description` | String   | Detailed description               |
| `price`       | Number   | Price in INR                       |
| `category`    | String   | Product category                   |
| `dimensions`  | String   | Size information                   |
| `materials`   | String   | What it's made of                  |
| `images`      | Array    | List of image URLs                 |
| `is_featured` | Boolean  | Show on homepage?                  |
| `is_new`      | Boolean  | Mark as new?                       |
| `created_at`  | Date     | When created                       |
| `updated_at`  | Date     | Last modified                      |

### 2. Reviews Collection

Stores customer reviews.

```json
// Collection: reviews
// Example document:
{
  "_id": "507f1f77bcf86cd799439022",
  "customer_name": "Priya Sharma",
  "customer_image": "https://res.cloudinary.com/xxx/avatar.jpg",
  "rating": 5,
  "review_text": "Absolutely beautiful coasters! The quality is amazing.",
  "product_name": "Ocean Wave Coaster Set",
  "is_featured": true,
  "created_at": "2024-01-20T14:00:00.000Z",
  "updated_at": "2024-01-20T14:00:00.000Z"
}
```

**Fields explained:**

| Field            | Type     | Description            |
| ---------------- | -------- | ---------------------- |
| `_id`            | ObjectId | Unique identifier      |
| `customer_name`  | String   | Customer's name        |
| `customer_image` | String   | Optional profile image |
| `rating`         | Number   | 1-5 stars              |
| `review_text`    | String   | The review content     |
| `product_name`   | String   | Which product reviewed |
| `is_featured`    | Boolean  | Show on homepage?      |
| `created_at`     | Date     | When created           |

### 3. Settings Collection

Stores site configuration. Uses a special `type` field to store different settings.

```json
// Collection: settings
// Document 1: Site settings
{
  "_id": "507f1f77bcf86cd799439033",
  "type": "site_settings",
  "whatsapp": "+91 9876543210",
  "instagram": "kalyani_resin_arts",
  "email": "contact@kalyaniresinarts.com",
  "address": "Hyderabad, India",
  "about_text": "We create beautiful handcrafted resin art...",
  "hero_title": "Welcome to Kalyani Resin Arts",
  "hero_subtitle": "Beautiful handcrafted resin art pieces",
  "footer_text": "© 2024 Kalyani Resin Arts"
}

// Document 2: Carousel slides
{
  "_id": "507f1f77bcf86cd799439044",
  "type": "carousel",
  "slides": [
    {
      "image": "https://res.cloudinary.com/xxx/slide1.jpg",
      "title": "New Collection",
      "subtitle": "Check out our latest designs"
    },
    {
      "image": "https://res.cloudinary.com/xxx/slide2.jpg",
      "title": "Handcrafted with Love",
      "subtitle": "Each piece is unique"
    }
  ]
}

// Document 3: Feature cards
{
  "_id": "507f1f77bcf86cd799439055",
  "type": "features",
  "cards": [
    {
      "icon": "🎨",
      "title": "Handcrafted",
      "description": "Every piece is made by hand"
    },
    {
      "icon": "✨",
      "title": "Unique Designs",
      "description": "No two pieces are alike"
    }
  ]
}
```

---

## How Collections Are Created

### The Magic: Auto-Creation! 🪄

**MongoDB creates collections automatically** when you first insert data into them.

You **DON'T** need to:

- Run any "CREATE TABLE" command
- Define a schema beforehand
- Manually create the collection

### How It Works

```python
# When you do this for the first time:
await db.products.insert_one({"name": "Ocean Coaster", "price": 899})

# MongoDB does this automatically:
# 1. Checks if 'products' collection exists
# 2. If not, CREATES it automatically
# 3. Inserts the document
```

### Step-by-Step: What Happens

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Your Code                                               │
│                                                                 │
│   db.products.insert_one({"name": "Ocean Coaster"})            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: MongoDB Checks                                          │
│                                                                 │
│   Does collection 'products' exist?                             │
│   ├── YES → Go to Step 4                                        │
│   └── NO  → Go to Step 3                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: MongoDB Creates Collection                              │
│                                                                 │
│   🆕 Creates 'products' collection automatically                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: MongoDB Inserts Document                                │
│                                                                 │
│   📝 Adds document to 'products' collection                     │
│   🔑 Generates _id automatically                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Example: First Product Insert

```python
# Your code (in routes/products.py):
@router.post("/products")
async def create_product(product: ProductCreate):
    db = get_database()

    product_dict = {
        "name": "Ocean Coaster",
        "price": 899,
        "category": "Coasters"
    }

    # This is the magic line!
    # If 'products' collection doesn't exist, MongoDB creates it
    result = await db.products.insert_one(product_dict)

    return {"id": str(result.inserted_id)}
```

### Verifying Collections Exist

You can check in MongoDB Atlas:

1. Go to your cluster
2. Click "Browse Collections"
3. You'll see all your collections listed

```
kalyani_resin_arts (Database)
├── products (3 documents)
├── reviews (5 documents)
└── settings (3 documents)
```

### Using the Seed Script

Our project has a `seed_data.py` script that creates sample data:

```python
# backend/seed_data.py

async def seed_products():
    db = client.get_database("kalyani_resin_arts")

    products = [
        {
            "name": "Ocean Wave Coaster Set",
            "price": 899,
            "category": "Coasters",
            # ... more fields
        },
        # ... more products
    ]

    # This creates 'products' collection if it doesn't exist
    # Then inserts all the products
    await db.products.insert_many(products)
```

**Run it:**

```bash
cd backend
python seed_data.py
```

---

## CRUD Operations Explained

CRUD = **C**reate, **R**ead, **U**pdate, **D**elete

### CREATE (Insert)

**Insert ONE document:**

```python
# Python with Motor
result = await db.products.insert_one({
    "name": "New Product",
    "price": 599
})

# result.inserted_id = the new document's _id
print(f"Created with ID: {result.inserted_id}")
```

**Insert MANY documents:**

```python
result = await db.products.insert_many([
    {"name": "Product 1", "price": 299},
    {"name": "Product 2", "price": 399},
    {"name": "Product 3", "price": 499}
])

# result.inserted_ids = list of all new _ids
print(f"Created {len(result.inserted_ids)} products")
```

**In our project (`routes/products.py`):**

```python
@router.post("/products")
async def create_product(product: ProductCreate):
    db = get_database()

    product_dict = product.model_dump()  # Convert to dictionary
    product_dict["created_at"] = datetime.utcnow()

    result = await db.products.insert_one(product_dict)

    product_dict["_id"] = str(result.inserted_id)
    return product_dict
```

### READ (Find)

**Find ALL documents:**

```python
# Get all products
products = await db.products.find().to_list(100)

# Result: List of all product documents
# [
#   {"_id": "...", "name": "Product 1", ...},
#   {"_id": "...", "name": "Product 2", ...}
# ]
```

**Find ONE document:**

```python
# Find by _id
from bson import ObjectId

product = await db.products.find_one({
    "_id": ObjectId("507f1f77bcf86cd799439011")
})

# Result: Single document or None
# {"_id": "...", "name": "Ocean Coaster", ...}
```

**Find with conditions:**

```python
# Find featured products
featured = await db.products.find({
    "is_featured": True
}).to_list(10)

# Find by category
coasters = await db.products.find({
    "category": "Coasters"
}).to_list(50)

# Find by price range
cheap = await db.products.find({
    "price": {"$lt": 500}  # Less than 500
}).to_list(50)
```

**In our project:**

```python
@router.get("/products")
async def get_all_products():
    db = get_database()

    products = await db.products.find().sort("created_at", -1).to_list(100)
    #                                  ↑
    #                    Sort by created_at, newest first (-1)

    return [serialize_product(p) for p in products]


@router.get("/products/{product_id}")
async def get_product(product_id: str):
    db = get_database()

    product = await db.products.find_one({
        "_id": ObjectId(product_id)
    })

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return serialize_product(product)
```

### UPDATE

**Update ONE document:**

```python
from bson import ObjectId
from datetime import datetime

result = await db.products.update_one(
    {"_id": ObjectId("507f1f77bcf86cd799439011")},  # Filter: which document
    {"$set": {                                       # Update: what to change
        "price": 999,
        "updated_at": datetime.utcnow()
    }}
)

# result.matched_count = how many matched the filter
# result.modified_count = how many were actually changed
```

**Update MANY documents:**

```python
# Make all coasters featured
result = await db.products.update_many(
    {"category": "Coasters"},     # Filter
    {"$set": {"is_featured": True}}  # Update
)

print(f"Updated {result.modified_count} products")
```

**In our project:**

```python
@router.put("/products/{product_id}")
async def update_product(product_id: str, product: ProductUpdate):
    db = get_database()

    # Only include fields that were sent (not None)
    update_data = {k: v for k, v in product.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()

    result = await db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    # Return the updated product
    updated = await db.products.find_one({"_id": ObjectId(product_id)})
    return serialize_product(updated)
```

### DELETE

**Delete ONE document:**

```python
result = await db.products.delete_one({
    "_id": ObjectId("507f1f77bcf86cd799439011")
})

# result.deleted_count = how many were deleted (0 or 1)
```

**Delete MANY documents:**

```python
# Delete all products in a category
result = await db.products.delete_many({
    "category": "Old Category"
})

print(f"Deleted {result.deleted_count} products")
```

**In our project:**

```python
@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    db = get_database()

    result = await db.products.delete_one({
        "_id": ObjectId(product_id)
    })

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return None  # 204 No Content
```

---

## Query Examples

### Comparison Operators

| Operator | Meaning          | Example                                          |
| -------- | ---------------- | ------------------------------------------------ |
| `$eq`    | Equal            | `{"price": {"$eq": 899}}`                        |
| `$ne`    | Not equal        | `{"category": {"$ne": "Coasters"}}`              |
| `$gt`    | Greater than     | `{"price": {"$gt": 500}}`                        |
| `$gte`   | Greater or equal | `{"price": {"$gte": 500}}`                       |
| `$lt`    | Less than        | `{"price": {"$lt": 1000}}`                       |
| `$lte`   | Less or equal    | `{"price": {"$lte": 1000}}`                      |
| `$in`    | In array         | `{"category": {"$in": ["Coasters", "Jewelry"]}}` |

### Example Queries

```python
# Products under ₹500
cheap_products = await db.products.find({
    "price": {"$lt": 500}
}).to_list(100)

# Featured AND New products
special = await db.products.find({
    "is_featured": True,
    "is_new": True
}).to_list(100)

# Products in Coasters OR Jewelry category
multi_category = await db.products.find({
    "category": {"$in": ["Coasters", "Jewelry"]}
}).to_list(100)

# Products with price between 500 and 1000
mid_range = await db.products.find({
    "price": {"$gte": 500, "$lte": 1000}
}).to_list(100)
```

### Sorting

```python
# Sort by price (ascending - low to high)
by_price_asc = await db.products.find().sort("price", 1).to_list(100)

# Sort by price (descending - high to low)
by_price_desc = await db.products.find().sort("price", -1).to_list(100)

# Sort by created_at (newest first)
newest_first = await db.products.find().sort("created_at", -1).to_list(100)

# Sort by multiple fields
multi_sort = await db.products.find().sort([
    ("is_featured", -1),  # Featured first
    ("created_at", -1)    # Then by newest
]).to_list(100)
```

### Limiting and Skipping

```python
# Get only first 10 products
first_10 = await db.products.find().limit(10).to_list(10)

# Skip first 10, get next 10 (pagination)
page_2 = await db.products.find().skip(10).limit(10).to_list(10)

# Pagination formula:
# skip = (page_number - 1) * items_per_page
# Page 1: skip(0).limit(10)
# Page 2: skip(10).limit(10)
# Page 3: skip(20).limit(10)
```

### Projection (Select specific fields)

```python
# Get only name and price (exclude other fields)
names_prices = await db.products.find(
    {},  # No filter (get all)
    {"name": 1, "price": 1}  # Only these fields (1 = include)
).to_list(100)

# Result:
# [
#   {"_id": "...", "name": "Product 1", "price": 899},
#   {"_id": "...", "name": "Product 2", "price": 599}
# ]

# Exclude specific fields
without_images = await db.products.find(
    {},
    {"images": 0, "description": 0}  # Exclude these (0 = exclude)
).to_list(100)
```

---

## Understanding ObjectId

### What is ObjectId?

ObjectId is MongoDB's default unique identifier. It's a 12-byte value:

```
507f1f77bcf86cd799439011
│       │     │    │
│       │     │    └── 3 bytes: counter (unique per machine)
│       │     └─────── 5 bytes: random value
│       └───────────── 4 bytes: timestamp (when created)
```

### Why ObjectId?

1. **Globally unique** - No collisions even across servers
2. **Contains timestamp** - You know when document was created
3. **Auto-generated** - No need to manage IDs yourself

### Working with ObjectId in Python

```python
from bson import ObjectId

# Create new ObjectId
new_id = ObjectId()
print(new_id)  # 507f1f77bcf86cd799439011

# Convert string to ObjectId (for queries)
string_id = "507f1f77bcf86cd799439011"
object_id = ObjectId(string_id)

# Check if string is valid ObjectId
ObjectId.is_valid("507f1f77bcf86cd799439011")  # True
ObjectId.is_valid("not-a-valid-id")            # False

# Convert ObjectId to string
str_id = str(object_id)  # "507f1f77bcf86cd799439011"
```

### In Our Project

```python
# routes/products.py

def serialize_product(product) -> dict:
    """Convert MongoDB document for JSON response"""
    if product:
        # Convert ObjectId to string (JSON can't handle ObjectId)
        product["_id"] = str(product["_id"])
    return product


@router.get("/products/{product_id}")
async def get_product(product_id: str):
    db = get_database()

    # Validate the ID format first
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    # Convert string to ObjectId for query
    product = await db.products.find_one({
        "_id": ObjectId(product_id)
    })

    return serialize_product(product)
```

---

## Connection String Explained

### Full Connection String

```
mongodb+srv://veera:veera7474@kalyaniresinarts.7mmmbo5.mongodb.net/kalyani_resin_arts?retryWrites=true&w=majority&appName=kalyaniresinarts
```

### Breaking It Down

```
mongodb+srv://         ← Protocol (SRV = modern DNS-based connection)
veera                  ← Username
:veera7474             ← Password
@kalyaniresinarts      ← Cluster name
.7mmmbo5.mongodb.net   ← MongoDB Atlas host
/kalyani_resin_arts    ← Database name
?retryWrites=true      ← Option: retry failed writes
&w=majority            ← Option: wait for majority acknowledgment
&appName=kalyaniresinarts ← Option: app name for monitoring
```

### Important Parts

| Part     | What It Is           | Example                                |
| -------- | -------------------- | -------------------------------------- |
| Protocol | Connection type      | `mongodb+srv://`                       |
| Username | Your database user   | `veera`                                |
| Password | User's password      | `veera7474`                            |
| Host     | MongoDB Atlas server | `kalyaniresinarts.7mmmbo5.mongodb.net` |
| Database | Default database     | `kalyani_resin_arts`                   |
| Options  | Connection settings  | `retryWrites=true`                     |

### Common Options

| Option             | Purpose                            |
| ------------------ | ---------------------------------- |
| `retryWrites=true` | Automatically retry failed writes  |
| `w=majority`       | Confirm write to majority of nodes |
| `authSource=admin` | Database for authentication        |
| `ssl=true`         | Use SSL (default for Atlas)        |

---

## Viewing Your Data

### Method 1: MongoDB Atlas UI

1. Go to https://cloud.mongodb.com
2. Select your cluster
3. Click "Browse Collections"
4. Select your database
5. Click on a collection to see documents

```
┌─────────────────────────────────────────────────────────────────┐
│ MongoDB Atlas                                                   │
├─────────────────────────────────────────────────────────────────┤
│ kalyani_resin_arts                                              │
│ ├── products                                                    │
│ │   └── [Click to view documents]                               │
│ ├── reviews                                                     │
│ └── settings                                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Method 2: MongoDB Compass (Desktop App)

1. Download: https://www.mongodb.com/products/compass
2. Install and open
3. Paste your connection string
4. Click "Connect"
5. Browse your data visually!

### Method 3: FastAPI Swagger UI

1. Start your backend: `uvicorn app.main:app --reload`
2. Go to http://localhost:8000/docs
3. Try the GET endpoints to see your data

### Method 4: Python Script

```python
# quick_check.py
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check_data():
    client = AsyncIOMotorClient("your-connection-string")
    db = client.kalyani_resin_arts

    # Count documents
    product_count = await db.products.count_documents({})
    review_count = await db.reviews.count_documents({})

    print(f"Products: {product_count}")
    print(f"Reviews: {review_count}")

    # Print first product
    first_product = await db.products.find_one()
    print(f"First product: {first_product}")

    client.close()

asyncio.run(check_data())
```

---

## Common Issues

### 1. Connection Refused

**Error:** `ServerSelectionTimeoutError: connection refused`

**Causes & Solutions:**

| Cause                 | Solution                                |
| --------------------- | --------------------------------------- |
| IP not whitelisted    | Add your IP in Atlas → Network Access   |
| Wrong password        | Check password in connection string     |
| Wrong cluster address | Copy connection string again from Atlas |

### 2. Authentication Failed

**Error:** `Authentication failed`

**Solutions:**

- Check username/password in connection string
- Make sure user exists in Atlas → Database Access
- Check the user has correct permissions

### 3. Database Not Found

**Error:** Your data isn't showing up

**Solutions:**

- Make sure database name is in connection string
- Check you're connected to correct cluster
- Verify collections exist using Atlas UI

### 4. Invalid ObjectId

**Error:** `Invalid ObjectId`

**Solution:**

```python
# Always validate before using
if not ObjectId.is_valid(product_id):
    raise HTTPException(status_code=400, detail="Invalid ID")
```

### 5. Timeout Errors

**Error:** `ServerSelectionTimeoutError`

**Solutions:**

- Check internet connection
- Verify Atlas cluster is running (check Atlas UI)
- Try adding `connectTimeoutMS=30000` to connection string

---

## Quick Reference

### MongoDB Operations Cheat Sheet

```python
# === CONNECT ===
from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient("mongodb+srv://...")
db = client.database_name

# === CREATE ===
await db.collection.insert_one({...})
await db.collection.insert_many([...])

# === READ ===
await db.collection.find().to_list(100)
await db.collection.find_one({"_id": ObjectId(id)})
await db.collection.find({"field": "value"}).to_list(100)

# === UPDATE ===
await db.collection.update_one({"_id": id}, {"$set": {...}})
await db.collection.update_many({filter}, {"$set": {...}})

# === DELETE ===
await db.collection.delete_one({"_id": id})
await db.collection.delete_many({filter})

# === HELPERS ===
await db.collection.count_documents({})
await db.collection.find().sort("field", -1).limit(10).to_list(10)
```

### Our Project's Collections

| Collection | Purpose        | Key Fields                         |
| ---------- | -------------- | ---------------------------------- |
| `products` | Store products | name, price, images, is_featured   |
| `reviews`  | Store reviews  | customer_name, rating, review_text |
| `settings` | Site config    | type, whatsapp, carousel slides    |

---

**🎉 You now understand MongoDB!**

Remember: MongoDB is flexible and forgiving. Collections are created automatically, and you can always add new fields to documents without changing anything else.

Happy coding! 🚀
