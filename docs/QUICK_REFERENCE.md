# 📋 Quick Reference Guide

A quick reference for common tasks in the Kalyani Resin Arts project.

---

## 🚀 Starting the Project

### Start Both Servers (Recommended for Development)

**Terminal 1 - Backend:**

```bash
cd backend
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**

```bash
cd frontend
npm run dev
```

### Access Points

- **Frontend**: http://localhost:5173
- **Admin Panel**: http://localhost:5173/admin
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## 📁 Where to Find Things

| I want to...             | Go to...                             |
| ------------------------ | ------------------------------------ |
| Add a new public page    | `frontend/src/pages/`                |
| Add a new admin page     | `frontend/src/pages/admin/`          |
| Modify navigation        | `frontend/src/components/Navbar.jsx` |
| Add a new API endpoint   | `backend/app/routes/`                |
| Add a new data model     | `backend/app/models/`                |
| Change API URL           | `frontend/.env`                      |
| Change database settings | `backend/.env`                       |
| Add a new component      | `frontend/src/components/`           |

---

## 🔧 Common Tasks

### Adding a New Product (Admin)

1. Go to http://localhost:5173/admin/login
2. Login with admin credentials
3. Navigate to Products
4. Click "Add Product"
5. Fill in details and save

### Adding a New API Endpoint

1. Create or modify file in `backend/app/routes/`
2. Add the route:

```python
@router.get("/your-endpoint")
async def your_function():
    return {"message": "Hello"}
```

3. If new file, register in `backend/app/main.py`:

```python
from app.routes import your_route
app.include_router(your_route.router, prefix="/api")
```

### Adding a New React Component

1. Create file in `frontend/src/components/`:

```jsx
// MyComponent.jsx
function MyComponent({ prop1, prop2 }) {
  return <div>{/* Your JSX */}</div>;
}

export default MyComponent;
```

2. Import and use:

```jsx
import MyComponent from "./components/MyComponent";

<MyComponent prop1="value" prop2={variable} />;
```

### Adding a New Page

1. Create page in `frontend/src/pages/`:

```jsx
// NewPage.jsx
function NewPage() {
  return <div>New Page Content</div>;
}
export default NewPage;
```

2. Add route in `frontend/src/App.jsx`:

```jsx
import NewPage from "./pages/NewPage";

<Route
  path="/new-page"
  element={
    <>
      <Navbar />
      <NewPage />
      <Footer />
    </>
  }
/>;
```

---

## 🛠 Debugging

### Frontend Issues

| Problem                | Solution                               |
| ---------------------- | -------------------------------------- |
| Blank page             | Check browser console (F12) for errors |
| API not working        | Check Network tab, is backend running? |
| Styles not applying    | Check CSS file import in component     |
| Component not updating | Check React DevTools for state         |

### Backend Issues

| Problem              | Solution                                 |
| -------------------- | ---------------------------------------- |
| Server won't start   | Check for syntax errors, is port in use? |
| MongoDB error        | Check connection string in `.env`        |
| 401 Unauthorized     | Check credentials, is token correct?     |
| 422 Validation error | Check request body matches model         |

### Quick Debug Commands

```bash
# Check if ports are in use
netstat -ano | findstr :8000
netstat -ano | findstr :5173

# Kill process on port (Windows)
taskkill /PID <pid> /F

# Check Python packages
pip list

# Check Node packages
npm list
```

---

## 📝 Common Code Patterns

### Fetching Data in React

```jsx
import { useState, useEffect } from "react";
import { productService } from "../services/api";

function MyComponent() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    productService
      .getAll()
      .then((res) => setData(res.data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {data.map((item) => (
        <div key={item._id}>{item.name}</div>
      ))}
    </div>
  );
}
```

### Creating a FastAPI Route

```python
from fastapi import APIRouter, HTTPException, Depends
from app.config.database import get_database
from app.auth.basic_auth import verify_credentials

router = APIRouter(prefix="/items", tags=["Items"])

# Public route
@router.get("")
async def get_all():
    db = get_database()
    items = await db.items.find().to_list(100)
    return items

# Protected route (admin only)
@router.post("")
async def create(
    data: dict,
    username: str = Depends(verify_credentials)
):
    db = get_database()
    result = await db.items.insert_one(data)
    return {"id": str(result.inserted_id)}
```

### Form Handling in React

```jsx
function MyForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    // Call API here
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={formData.name} onChange={handleChange} />
      <input name="email" value={formData.email} onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

---

## 🔐 Authentication Quick Reference

### Frontend - Login

```javascript
import { authService } from "../services/api";

// Login
await authService.login("admin", "password");

// Check if logged in
const isLoggedIn = authService.isAuthenticated();

// Logout
authService.logout();
```

### Backend - Protect Route

```python
from app.auth.basic_auth import verify_credentials
from fastapi import Depends

@router.post("/protected")
async def protected_route(
    username: str = Depends(verify_credentials)
):
    # Only reaches here if authenticated
    return {"user": username}
```

---

## 📦 Package Management

### Frontend (npm)

```bash
# Install all dependencies
npm install

# Add a new package
npm install package-name

# Add dev dependency
npm install -D package-name

# Update all packages
npm update
```

### Backend (pip)

```bash
# Activate virtual environment first!
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Add a new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

---

## 🌐 Environment Variables

### Frontend (Vite)

```env
# Must start with VITE_
VITE_API_URL=/api
VITE_SOME_KEY=value
```

Access in code:

```javascript
const apiUrl = import.meta.env.VITE_API_URL;
```

### Backend (Python)

```env
MONGODB_URL=your-url
ADMIN_USERNAME=admin
```

Access in code (via settings.py):

```python
from app.config.settings import settings

url = settings.mongodb_url
```

---

## 🚨 Error Codes

| Code | Meaning          | Common Cause              |
| ---- | ---------------- | ------------------------- |
| 200  | OK               | Success                   |
| 201  | Created          | POST successful           |
| 204  | No Content       | DELETE successful         |
| 400  | Bad Request      | Invalid data              |
| 401  | Unauthorized     | Bad credentials           |
| 404  | Not Found        | Resource doesn't exist    |
| 422  | Validation Error | Data doesn't match schema |
| 500  | Server Error     | Backend crashed           |

---

## 📚 Useful Links

- [React Docs](https://react.dev/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [MongoDB Docs](https://www.mongodb.com/docs/)
- [Axios Docs](https://axios-http.com/)
- [Vite Docs](https://vitejs.dev/)

---

**💡 Tip:** Bookmark this page for quick access!
