# 🎨 Kalyani Resin Arts - Complete Project Documentation

<p align="center">
  <strong>A Full-Stack E-commerce Showcase for Handcrafted Resin Art</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-React%20+%20Vite-61DAFB?style=for-the-badge&logo=react" alt="React">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Database-MongoDB-47A248?style=for-the-badge&logo=mongodb" alt="MongoDB">
  <img src="https://img.shields.io/badge/Deploy-Vercel-000000?style=for-the-badge&logo=vercel" alt="Vercel">
</p>

---

## 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [Architecture](#-architecture)
3. [Quick Start](#-quick-start)
4. [Project Structure](#-project-structure)
5. [Features](#-features)
6. [Technology Stack](#-technology-stack)
7. [Documentation](#-documentation)
8. [Environment Setup](#-environment-setup)
9. [API Overview](#-api-overview)
10. [Deployment](#-deployment)
11. [Contributing](#-contributing)

---

## 🎯 Project Overview

**Kalyani Resin Arts** is a modern e-commerce showcase website for a resin arts business. The project consists of:

- **Public Website**: Beautiful product gallery, homepage with carousel, customer reviews
- **Admin Panel**: Manage products, reviews, and site settings
- **Backend API**: RESTful API with MongoDB database

### What Problem Does This Solve?

This project provides a small business with:

- ✅ Professional online presence
- ✅ Product catalog management
- ✅ Easy content updates (no coding needed)
- ✅ Customer review showcase
- ✅ Contact information display

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                │
│                    (React + Vite)                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Public     │  │    Admin     │  │  Components  │          │
│  │   Pages      │  │    Panel     │  │  & Services  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP Requests (REST API)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND                                 │
│                       (FastAPI)                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Routes     │  │   Models     │  │     Auth     │          │
│  │  (API Ends)  │  │  (Schemas)   │  │ (Basic Auth) │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Database Queries
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATABASE                                 │
│                       (MongoDB)                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Products    │  │   Reviews    │  │   Settings   │          │
│  │ Collection   │  │  Collection  │  │  Collection  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

### How Data Flows

1. **User visits website** → React frontend loads
2. **Frontend needs data** → Calls backend API (e.g., `/api/products`)
3. **Backend receives request** → Queries MongoDB
4. **MongoDB returns data** → Backend formats response
5. **Frontend receives data** → Displays to user

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **Python** 3.9+ ([Download](https://python.org/))
- **MongoDB** account ([MongoDB Atlas](https://mongodb.com/atlas) - free tier available)

### Clone the Repository

```bash
git clone <repository-url>
cd Kalyani_resin_arts
```

### Start Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from example or create new)
# Add your MongoDB URL and other settings

# Start server
uvicorn app.main:app --reload
```

Backend runs at: http://localhost:8000

### Start Frontend

```bash
# Open new terminal, navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs at: http://localhost:5173

### Access Points

| URL                         | Description                 |
| --------------------------- | --------------------------- |
| http://localhost:5173       | Frontend (Public Website)   |
| http://localhost:5173/admin | Admin Panel                 |
| http://localhost:8000       | Backend API Root            |
| http://localhost:8000/docs  | API Documentation (Swagger) |

---

## 📁 Project Structure

```
Kalyani_resin_arts/
│
├── 📁 frontend/                 # React + Vite Frontend
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   │   ├── Navbar.jsx       # Navigation bar
│   │   │   ├── Footer.jsx       # Site footer
│   │   │   ├── ProductCard.jsx  # Product display card
│   │   │   ├── ImageGallery.jsx # Image viewer
│   │   │   ├── AdminLayout.jsx  # Admin page layout
│   │   │   └── ProtectedRoute.jsx # Auth guard
│   │   │
│   │   ├── pages/               # Page components
│   │   │   ├── Home.jsx         # Homepage
│   │   │   ├── Products.jsx     # All products
│   │   │   ├── ProductDetail.jsx # Single product
│   │   │   ├── Contact.jsx      # Contact info
│   │   │   └── admin/           # Admin pages
│   │   │       ├── AdminLogin.jsx
│   │   │       ├── AdminDashboard.jsx
│   │   │       ├── AdminProducts.jsx
│   │   │       ├── AdminReviews.jsx
│   │   │       └── AdminSettings.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js           # API service layer
│   │   │
│   │   ├── App.jsx              # Main app with routes
│   │   └── main.jsx             # Entry point
│   │
│   ├── package.json
│   └── vite.config.js
│
├── 📁 backend/                  # FastAPI Backend
│   ├── app/
│   │   ├── auth/
│   │   │   └── basic_auth.py    # Authentication logic
│   │   │
│   │   ├── config/
│   │   │   ├── database.py      # MongoDB connection
│   │   │   └── settings.py      # App configuration
│   │   │
│   │   ├── models/
│   │   │   ├── product.py       # Product schema
│   │   │   ├── review.py        # Review schema
│   │   │   └── settings.py      # Settings schema
│   │   │
│   │   ├── routes/
│   │   │   ├── auth.py          # Auth endpoints
│   │   │   ├── products.py      # Product CRUD
│   │   │   ├── reviews.py       # Review CRUD
│   │   │   ├── settings.py      # Settings endpoints
│   │   │   └── upload.py        # Image upload
│   │   │
│   │   └── main.py              # FastAPI app entry
│   │
│   ├── requirements.txt
│   └── seed_data.py             # Sample data script
│
├── 📁 docs/                     # Documentation
│   ├── FRONTEND_DOCUMENTATION.md
│   └── BACKEND_DOCUMENTATION.md
│
├── vercel.json                  # Vercel deployment config
└── README.md                    # This file
```

---

## ✨ Features

### Public Website

| Feature               | Description                                        |
| --------------------- | -------------------------------------------------- |
| 🏠 **Homepage**       | Hero carousel, featured products, customer reviews |
| 📦 **Products Page**  | Browse all products with categories                |
| 🔍 **Product Detail** | Full product info with image gallery               |
| 📞 **Contact Page**   | WhatsApp, Instagram, email, address                |

### Admin Panel

| Feature                   | Description                             |
| ------------------------- | --------------------------------------- |
| 🔐 **Secure Login**       | HTTP Basic Authentication               |
| 📦 **Product Management** | Add, edit, delete products              |
| ⭐ **Review Management**  | Manage customer testimonials            |
| ⚙️ **Site Settings**      | Update contact info, carousel, features |
| 🖼️ **Image Upload**       | Upload to Cloudinary                    |

---

## 🛠 Technology Stack

### Frontend

| Package          | Version | Purpose       |
| ---------------- | ------- | ------------- |
| React            | 18.2.0  | UI library    |
| Vite             | 5.0.0   | Build tool    |
| React Router DOM | 6.20.0  | Navigation    |
| Axios            | 1.6.2   | HTTP client   |
| React Icons      | 4.12.0  | Icon library  |
| React Toastify   | 9.1.3   | Notifications |
| Swiper           | 11.0.5  | Carousels     |

### Backend

| Package    | Version | Purpose              |
| ---------- | ------- | -------------------- |
| FastAPI    | 0.104.1 | Web framework        |
| Uvicorn    | 0.24.0  | ASGI server          |
| Motor      | 3.3.2   | Async MongoDB driver |
| Pydantic   | 2.5.2   | Data validation      |
| Cloudinary | 1.36.0  | Image hosting        |

---

## 📚 Documentation

Detailed documentation is available in the `docs/` folder:

| Document                                            | Description                           |
| --------------------------------------------------- | ------------------------------------- |
| [Frontend Documentation](FRONTEND_DOCUMENTATION.md) | Complete guide to the React frontend  |
| [Backend Documentation](BACKEND_DOCUMENTATION.md)   | Complete guide to the FastAPI backend |
| [MongoDB Guide](MONGODB_GUIDE.md)                   | End-to-end MongoDB database guide     |
| [Quick Reference](QUICK_REFERENCE.md)               | Common tasks and code patterns        |

### What's Covered

**Frontend Documentation:**

- Component breakdown
- Page explanations
- API service layer
- Routing system
- Styling guide
- Deployment steps

**Backend Documentation:**

- FastAPI basics
- MongoDB operations
- API routes explained
- Models and validation
- Authentication
- Image upload

**MongoDB Guide:**

- What is MongoDB (beginner explanation)
- MongoDB vs SQL databases
- Collections and Documents
- How collections are auto-created
- CRUD operations with examples
- Query operators and examples
- MongoDB Atlas setup
- Connection string explained

---

## ⚙️ Environment Setup

### Backend Environment Variables

Create `backend/.env`:

```env
# MongoDB Connection
MONGODB_URL=mongodb+srv://user:pass@cluster.mongodb.net/database

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-secure-password

# Debug Mode
DEBUG=true

# CORS - Allowed Frontend Origins
ALLOWED_ORIGINS=http://localhost:5173,https://your-domain.com

# Cloudinary (for image uploads)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### Frontend Environment Variables

Create `frontend/.env`:

```env
# API URL (backend)
VITE_API_URL=/api
```

---

## 📡 API Overview

### Endpoints Summary

| Category     | Endpoints                                      | Auth Required  |
| ------------ | ---------------------------------------------- | -------------- |
| **Products** | GET, POST, PUT, DELETE `/api/products`         | Write ops only |
| **Reviews**  | GET, POST, PUT, DELETE `/api/reviews`          | Write ops only |
| **Settings** | GET, PUT `/api/settings`                       | Write ops only |
| **Auth**     | POST `/api/auth/login`, GET `/api/auth/verify` | Yes            |
| **Upload**   | POST, DELETE `/api/upload`                     | Yes            |

### Example Request

```bash
# Get all products (public)
curl http://localhost:8000/api/products

# Create product (admin only)
curl -X POST http://localhost:8000/api/products \
  -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Product", "price": 999}'
```

### Full API Documentation

Visit http://localhost:8000/docs for interactive API documentation (Swagger UI).

---

## 🚀 Deployment

### Vercel Deployment (Recommended)

This project is configured for Vercel deployment.

#### Steps:

1. **Push to GitHub**

   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Import to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Select your GitHub repository

3. **Configure Environment Variables**

   Add these in Vercel dashboard:
   - `MONGODB_URL`
   - `ADMIN_USERNAME`
   - `ADMIN_PASSWORD`
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`

4. **Deploy!**

### Production Checklist

- [ ] Change default admin password
- [ ] Set up MongoDB Atlas with IP whitelist
- [ ] Configure Cloudinary account
- [ ] Update `ALLOWED_ORIGINS` with production URL
- [ ] Set `DEBUG=false`

---

## 🤝 Contributing

### For Junior Developers

1. **Read the documentation first** - Understanding the codebase is crucial
2. **Start small** - Fix a bug or add a small feature
3. **Ask questions** - Don't hesitate to ask for help
4. **Follow the patterns** - Look at existing code for examples

### Development Workflow

```bash
# 1. Create a new branch
git checkout -b feature/your-feature-name

# 2. Make your changes
# ... code ...

# 3. Test locally
npm run dev  # frontend
uvicorn app.main:app --reload  # backend

# 4. Commit your changes
git add .
git commit -m "Add: description of your changes"

# 5. Push and create PR
git push origin feature/your-feature-name
```

### Code Style

- **Frontend**: Follow React best practices, use functional components
- **Backend**: Follow PEP 8, use type hints

---

## 📞 Support

If you're stuck:

1. **Check the documentation** in `docs/` folder
2. **Check the console** for error messages
3. **Search the error** online
4. **Ask the team** for help

---

## 📄 License

This project is private and proprietary to Kalyani Resin Arts.

---

<p align="center">
  Made with ❤️ for Kalyani Resin Arts
</p>
