# 📦 Frontend Documentation - Kalyani Resin Arts

## Table of Contents

1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Environment Setup](#environment-setup)
6. [Understanding Components](#understanding-components)
7. [Pages Explained](#pages-explained)
8. [Services (API Layer)](#services-api-layer)
9. [Routing](#routing)
10. [Styling Guide](#styling-guide)
11. [Deployment](#deployment)
12. [Troubleshooting](#troubleshooting)

---

## Introduction

Welcome! 👋 This documentation is designed for junior developers who are new to the project. We'll explain everything step by step.

**What is this project?**

Kalyani Resin Arts is an e-commerce showcase website for a resin arts business. The frontend is the part users see and interact with - it displays products, handles navigation, and provides an admin panel for managing content.

**What does the Frontend do?**

- ✅ Displays products in a beautiful gallery
- ✅ Shows featured products on the homepage
- ✅ Handles customer reviews display
- ✅ Provides contact information
- ✅ Admin panel for managing products, reviews, and settings

---

## Technology Stack

Here's what we use and why:

| Technology           | Version | Purpose                                                  |
| -------------------- | ------- | -------------------------------------------------------- |
| **React**            | 18.2.0  | UI library for building user interfaces                  |
| **Vite**             | 5.0.0   | Fast build tool and development server                   |
| **React Router DOM** | 6.20.0  | Handles page navigation (going from one page to another) |
| **Axios**            | 1.6.2   | Makes HTTP requests to our backend API                   |
| **React Icons**      | 4.12.0  | Provides beautiful icons                                 |
| **React Toastify**   | 9.1.3   | Shows popup notifications (success, error messages)      |
| **Swiper**           | 11.0.5  | Creates beautiful image carousels/sliders                |

### What is React? (For Beginners)

React is a JavaScript library that helps us build user interfaces. Instead of writing HTML directly, we write **components** - small, reusable pieces of UI.

### What is Vite?

Vite (pronounced "veet") is a build tool that:

- Starts your development server super fast ⚡
- Hot-reloads when you save files (you see changes instantly)
- Builds optimized code for production

---

## Project Structure

```
frontend/
├── index.html              # Main HTML file (entry point)
├── package.json            # Lists all dependencies and scripts
├── vite.config.js          # Vite configuration
├── vercel.json             # Vercel deployment settings
├── .env.example            # Example environment variables
│
├── public/                 # Static files (favicons, etc.)
│
└── src/                    # All our source code lives here
    ├── main.jsx            # React app entry point
    ├── App.jsx             # Main app component with routes
    ├── index.css           # Global styles
    │
    ├── components/         # Reusable UI pieces
    │   ├── Navbar.jsx      # Navigation bar
    │   ├── Navbar.css
    │   ├── Footer.jsx      # Website footer
    │   ├── Footer.css
    │   ├── ProductCard.jsx # Single product display card
    │   ├── ProductCard.css
    │   ├── ImageGallery.jsx # Image viewer component
    │   ├── ImageGallery.css
    │   ├── AdminLayout.jsx  # Layout for admin pages
    │   ├── AdminLayout.css
    │   └── ProtectedRoute.jsx # Guards admin routes
    │
    ├── pages/              # Full page components
    │   ├── Home.jsx        # Homepage
    │   ├── Home.css
    │   ├── Products.jsx    # All products page
    │   ├── Products.css
    │   ├── ProductDetail.jsx # Single product page
    │   ├── ProductDetail.css
    │   ├── Contact.jsx     # Contact page
    │   ├── Contact.css
    │   │
    │   └── admin/          # Admin panel pages
    │       ├── AdminLogin.jsx      # Admin login page
    │       ├── AdminLogin.css
    │       ├── AdminDashboard.jsx  # Admin home
    │       ├── AdminProducts.jsx   # Manage products
    │       ├── AdminProducts.css
    │       ├── AdminReviews.jsx    # Manage reviews
    │       ├── AdminReviews.css
    │       ├── AdminSettings.jsx   # Site settings
    │       └── AdminSettings.css
    │
    └── services/
        └── api.js          # All API calls to backend
```

### Understanding the Structure

**Think of it like a house:**

- `index.html` = The front door (entry point)
- `src/` = All the rooms inside
- `components/` = Furniture (reusable pieces)
- `pages/` = Different rooms (Home, Products, etc.)
- `services/` = Utilities (plumbing, electricity - API calls)

---

## Getting Started

### Prerequisites

Before you start, make sure you have:

1. **Node.js** (version 18 or higher)
   - Download from: https://nodejs.org/
   - Verify: `node --version`

2. **npm** (comes with Node.js)
   - Verify: `npm --version`

### Installation Steps

```bash
# Step 1: Navigate to the frontend folder
cd frontend

# Step 2: Install all dependencies
npm install

# Step 3: Start the development server
npm run dev
```

After running `npm run dev`, you'll see:

```
  VITE v5.0.0  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: http://192.168.1.100:5173/
```

Open http://localhost:5173 in your browser! 🎉

### Available Scripts

| Command           | What it does                                     |
| ----------------- | ------------------------------------------------ |
| `npm run dev`     | Starts development server with hot-reload        |
| `npm run build`   | Creates production-ready files in `dist/` folder |
| `npm run preview` | Preview the production build locally             |
| `npm run lint`    | Check for code quality issues                    |

---

## Environment Setup

### What are Environment Variables?

Environment variables are settings that can change between environments (development, production). We use them to store:

- API URLs
- Secret keys (never commit these!)

### Setting Up

1. Copy the example file:

```bash
cp .env.example .env
```

2. Edit `.env`:

```env
# The URL where our backend API is running
VITE_API_URL=/api
```

**Important Notes:**

- In Vite, environment variables must start with `VITE_`
- Access them in code with: `import.meta.env.VITE_API_URL`
- Never commit `.env` files with secrets!

---

## Understanding Components

### What is a Component?

A component is a reusable piece of UI. Think of it like LEGO blocks - you build your UI by combining smaller pieces.

### Component Breakdown

#### 1. Navbar Component (`Navbar.jsx`)

**Purpose:** The navigation bar at the top of every page.

**What it does:**

- Shows the logo
- Links to different pages (Home, Products, Contact)
- Responsive (changes on mobile)

**Simple explanation:**

```jsx
function Navbar() {
  return (
    <nav className="navbar">
      {/* Logo on the left */}
      <div className="logo">
        <Link to="/">Kalyani Resin Arts</Link>
      </div>

      {/* Navigation links on the right */}
      <ul className="nav-links">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/products">Products</Link>
        </li>
        <li>
          <Link to="/contact">Contact</Link>
        </li>
      </ul>
    </nav>
  );
}
```

#### 2. ProductCard Component (`ProductCard.jsx`)

**Purpose:** Displays a single product in a card format.

**Props it receives:**

- `product` - The product data object

**What it shows:**

- Product image
- Product name
- Price
- "New" badge if it's new
- "Featured" badge if featured

**Usage:**

```jsx
<ProductCard product={productData} />
```

#### 3. ProtectedRoute Component (`ProtectedRoute.jsx`)

**Purpose:** Guards admin pages - only logged-in admins can access them.

**How it works:**

```jsx
function ProtectedRoute({ children }) {
  // Step 1: Check if user is authenticated
  const [isAuth, setIsAuth] = useState(null);

  useEffect(() => {
    // Step 2: Verify the token with backend
    if (!authService.isAuthenticated()) {
      setIsAuth(false);
      return;
    }

    authService
      .verifyToken()
      .then(() => setIsAuth(true)) // Token valid
      .catch(() => {
        authService.logout(); // Token invalid
        setIsAuth(false);
      });
  }, []);

  // Step 3: Show loading while checking
  if (isAuth === null) {
    return <div className="loading">Loading...</div>;
  }

  // Step 4: Redirect to login if not authenticated
  // Otherwise, show the protected content
  return isAuth ? children : <Navigate to="/admin/login" />;
}
```

#### 4. ImageGallery Component (`ImageGallery.jsx`)

**Purpose:** Shows product images with ability to click and enlarge.

**Features:**

- Thumbnail strip at bottom
- Main image display
- Click to change main image
- Lightbox for full-size viewing

---

## Pages Explained

### Public Pages (Anyone can access)

#### 1. Home Page (`Home.jsx`)

**URL:** `/`

**What it displays:**

- Hero carousel (big image slider at top)
- About section with feature cards
- Featured products grid
- Customer reviews carousel

**Data it fetches:**

```javascript
// All data fetched when page loads
Promise.all([
  productService.getFeatured(), // Featured products
  settingsService.getCarousel(), // Carousel images
  settingsService.get(), // Site settings
  reviewService.getFeatured(), // Customer reviews
  settingsService.getFeatures(), // Feature cards
]);
```

#### 2. Products Page (`Products.jsx`)

**URL:** `/products`

**What it displays:**

- Grid of all products
- Category filter (optional)
- Search functionality

#### 3. Product Detail Page (`ProductDetail.jsx`)

**URL:** `/products/:id`

**What `:id` means:** It's a dynamic parameter. If you visit `/products/123`, the `id` will be `123`.

**What it displays:**

- Large product images
- Full description
- Price, dimensions, materials
- Image gallery

#### 4. Contact Page (`Contact.jsx`)

**URL:** `/contact`

**What it displays:**

- Business contact information
- WhatsApp link
- Instagram link
- Email
- Address

### Admin Pages (Login Required)

#### 1. Admin Login (`AdminLogin.jsx`)

**URL:** `/admin/login`

**What it does:**

- Shows username/password form
- Validates credentials with backend
- Stores authentication token
- Redirects to dashboard on success

**How login works:**

```javascript
// When user submits login form
const handleLogin = async (username, password) => {
  try {
    // authService.login sends credentials to backend
    await authService.login(username, password);

    // If successful, redirect to admin dashboard
    navigate("/admin");
  } catch (error) {
    // Show error message
    toast.error("Invalid credentials");
  }
};
```

#### 2. Admin Dashboard (`AdminDashboard.jsx`)

**URL:** `/admin`

**What it displays:**

- Overview statistics
- Quick links to manage products, reviews, settings

#### 3. Admin Products (`AdminProducts.jsx`)

**URL:** `/admin/products`

**Features:**

- List all products
- Add new product
- Edit existing product
- Delete product
- Upload product images
- Search/filter products

**CRUD Operations explained:**

```javascript
// CREATE - Add new product
const createProduct = async (productData) => {
  await productService.create(productData);
};

// READ - Get all products
const loadProducts = async () => {
  const response = await productService.getAll();
  setProducts(response.data);
};

// UPDATE - Edit product
const updateProduct = async (id, productData) => {
  await productService.update(id, productData);
};

// DELETE - Remove product
const deleteProduct = async (id) => {
  await productService.delete(id);
};
```

#### 4. Admin Reviews (`AdminReviews.jsx`)

**URL:** `/admin/reviews`

**Features:**

- Manage customer reviews
- Add/edit/delete reviews
- Toggle featured status

#### 5. Admin Settings (`AdminSettings.jsx`)

**URL:** `/admin/settings`

**What you can configure:**

- Site information (WhatsApp, Instagram, Email)
- Hero section text
- Carousel images
- Feature cards
- Footer text

---

## Services (API Layer)

### What is `api.js`?

The `services/api.js` file is our **API layer**. It handles all communication with the backend server.

### Why use a separate API layer?

1. **Centralized** - All API calls in one place
2. **Reusable** - Call the same functions from anywhere
3. **Maintainable** - Easy to update API endpoints
4. **Clean** - Components don't need to know about HTTP details

### Axios Setup

```javascript
import axios from "axios";

// Create an axios instance with default settings
const API_URL = import.meta.env.VITE_API_URL || "/api";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptor: Automatically add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("adminToken");
  if (token) {
    config.headers.Authorization = `Basic ${token}`;
  }
  return config;
});
```

### Available Services

#### Product Service

```javascript
export const productService = {
  // Get all products
  getAll: () => api.get("/products"),

  // Get single product by ID
  getById: (id) => api.get(`/products/${id}`),

  // Get featured products only
  getFeatured: () => api.get("/products/featured"),

  // Create new product (admin only)
  create: (data) => api.post("/products", data),

  // Update existing product (admin only)
  update: (id, data) => api.put(`/products/${id}`, data),

  // Delete product (admin only)
  delete: (id) => api.delete(`/products/${id}`),

  // Upload product image (admin only)
  uploadImage: (file) => {
    const formData = new FormData();
    formData.append("file", file);
    return api.post("/upload", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
  },
};
```

#### Settings Service

```javascript
export const settingsService = {
  // Get site settings
  get: () => api.get("/settings"),

  // Update site settings (admin only)
  update: (data) => api.put("/settings", data),

  // Get carousel slides
  getCarousel: () => api.get("/settings/carousel"),

  // Update carousel slides (admin only)
  updateCarousel: (data) => api.put("/settings/carousel", data),

  // Get feature cards
  getFeatures: () => api.get("/settings/features"),

  // Update feature cards (admin only)
  updateFeatures: (data) => api.put("/settings/features", data),
};
```

#### Review Service

```javascript
export const reviewService = {
  // Get all reviews
  getAll: () => api.get("/reviews"),

  // Get single review
  getById: (id) => api.get(`/reviews/${id}`),

  // Get featured reviews for homepage
  getFeatured: () => api.get("/reviews/featured"),

  // Create new review (admin only)
  create: (data) => api.post("/reviews", data),

  // Update review (admin only)
  update: (id, data) => api.put(`/reviews/${id}`, data),

  // Delete review (admin only)
  delete: (id) => api.delete(`/reviews/${id}`),
};
```

#### Auth Service

```javascript
export const authService = {
  // Login with username and password
  login: (username, password) => {
    // Create base64 encoded token (Basic Auth)
    const token = btoa(`${username}:${password}`);

    return api
      .post(
        "/auth/login",
        {},
        {
          headers: { Authorization: `Basic ${token}` },
        },
      )
      .then((response) => {
        // Store token for future requests
        localStorage.setItem("adminToken", token);
        return response;
      });
  },

  // Logout - remove stored token
  logout: () => {
    localStorage.removeItem("adminToken");
  },

  // Check if user has token stored
  isAuthenticated: () => {
    return !!localStorage.getItem("adminToken");
  },

  // Verify token is still valid with backend
  verifyToken: () => api.get("/auth/verify"),
};
```

### How to Use Services in Components

```jsx
import { productService } from "../services/api";
import { useState, useEffect } from "react";

function MyComponent() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch products when component mounts
    productService
      .getAll()
      .then((response) => {
        setProducts(response.data); // response.data contains the actual data
      })
      .catch((error) => {
        console.error("Failed to load products:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []); // Empty array means run once on mount

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {products.map((product) => (
        <div key={product._id}>{product.name}</div>
      ))}
    </div>
  );
}
```

---

## Routing

### What is React Router?

React Router lets us navigate between pages without full page reloads. It's what makes our app a **Single Page Application (SPA)**.

### Route Configuration (`App.jsx`)

```jsx
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="app">
      <Routes>
        {/* PUBLIC ROUTES - Anyone can access */}
        <Route
          path="/"
          element={
            <>
              <Navbar />
              <Home />
              <Footer />
            </>
          }
        />

        <Route
          path="/products"
          element={
            <>
              <Navbar />
              <Products />
              <Footer />
            </>
          }
        />

        <Route
          path="/products/:id"
          element={
            <>
              <Navbar />
              <ProductDetail />
              <Footer />
            </>
          }
        />

        <Route
          path="/contact"
          element={
            <>
              <Navbar />
              <Contact />
              <Footer />
            </>
          }
        />

        {/* ADMIN ROUTES - Login required */}
        <Route path="/admin/login" element={<AdminLogin />} />

        <Route
          path="/admin"
          element={
            <ProtectedRoute>
              <AdminDashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/admin/products"
          element={
            <ProtectedRoute>
              <AdminProducts />
            </ProtectedRoute>
          }
        />

        <Route
          path="/admin/reviews"
          element={
            <ProtectedRoute>
              <AdminReviews />
            </ProtectedRoute>
          }
        />

        <Route
          path="/admin/settings"
          element={
            <ProtectedRoute>
              <AdminSettings />
            </ProtectedRoute>
          }
        />
      </Routes>
    </div>
  );
}
```

### Understanding Routes

| Path              | Component      | Description                               |
| ----------------- | -------------- | ----------------------------------------- |
| `/`               | Home           | Homepage with carousel, featured products |
| `/products`       | Products       | All products listing                      |
| `/products/:id`   | ProductDetail  | Single product view (`:id` is dynamic)    |
| `/contact`        | Contact        | Contact information page                  |
| `/admin/login`    | AdminLogin     | Admin login form                          |
| `/admin`          | AdminDashboard | Admin homepage (protected)                |
| `/admin/products` | AdminProducts  | Manage products (protected)               |
| `/admin/reviews`  | AdminReviews   | Manage reviews (protected)                |
| `/admin/settings` | AdminSettings  | Site settings (protected)                 |

### Navigation

Use the `Link` component for navigation:

```jsx
import { Link } from 'react-router-dom'

// Navigate to products page
<Link to="/products">View Products</Link>

// Navigate with dynamic ID
<Link to={`/products/${product._id}`}>View Details</Link>
```

Use `useNavigate` for programmatic navigation:

```jsx
import { useNavigate } from "react-router-dom";

function MyComponent() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/admin"); // Redirect to admin page
  };

  return <button onClick={handleClick}>Go to Admin</button>;
}
```

---

## Styling Guide

### CSS Organization

Each component/page has its own CSS file:

- `Navbar.jsx` → `Navbar.css`
- `Home.jsx` → `Home.css`

### Global Styles (`index.css`)

Contains:

- CSS reset/normalize
- CSS custom properties (variables)
- Utility classes
- Common animations

### CSS Custom Properties (Variables)

Use consistent colors across the app:

```css
:root {
  --primary-color: #your-primary-color;
  --secondary-color: #your-secondary-color;
  --text-color: #333333;
  --background-color: #ffffff;
}
```

Usage:

```css
.button {
  background-color: var(--primary-color);
}
```

### Responsive Design

We use media queries for responsiveness:

```css
/* Mobile first approach */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

---

## Deployment

### Vercel Deployment (Recommended)

Our project is configured for Vercel deployment.

**vercel.json configuration:**

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "framework": "vite",
  "rewrites": [{ "source": "/(.*)", "destination": "/" }]
}
```

**Why the rewrite rule?**

- This handles client-side routing
- All paths redirect to `index.html`
- React Router then handles the actual routing

### Deployment Steps

1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables in Vercel:
   - `VITE_API_URL` = Your backend API URL
4. Deploy!

### Building for Production

```bash
# Create optimized build
npm run build

# Preview the build locally
npm run preview
```

The `dist/` folder contains the production-ready files.

---

## Troubleshooting

### Common Issues

#### 1. "Module not found" Error

**Solution:** Install dependencies

```bash
npm install
```

#### 2. Blank Page After Build

**Possible causes:**

- Wrong base URL in `vite.config.js`
- Missing environment variables

**Check console for errors** (F12 → Console tab)

#### 3. API Calls Failing

**Check:**

- Is the backend running?
- Is `VITE_API_URL` set correctly?
- Check Network tab in browser DevTools

#### 4. Images Not Loading

**Check:**

- Correct image URL?
- CORS enabled on backend?
- Image file exists?

#### 5. Login Not Working

**Check:**

- Backend is running
- Correct username/password
- Token stored in localStorage
- Network tab for error details

### Debugging Tips

1. **Use console.log()** to trace execution

```javascript
console.log("Data received:", data);
```

2. **Check Network tab** (F12 → Network) for API calls

3. **Check React DevTools** for component state

4. **Read error messages carefully** - they usually tell you what's wrong!

---

## Quick Reference

### File to Edit for...

| Task                 | File                                      |
| -------------------- | ----------------------------------------- |
| Add new page         | `src/pages/NewPage.jsx` + `App.jsx` route |
| Modify navigation    | `src/components/Navbar.jsx`               |
| Change API URL       | `.env` file                               |
| Add new API endpoint | `src/services/api.js`                     |
| Modify product card  | `src/components/ProductCard.jsx`          |
| Change global styles | `src/index.css`                           |

### Useful Links

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [React Router Documentation](https://reactrouter.com/)
- [Axios Documentation](https://axios-http.com/)
- [Swiper Documentation](https://swiperjs.com/react)

---

**Happy Coding! 🚀**

If you have questions, check the code comments or reach out to the team.
