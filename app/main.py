from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config.settings import settings
from app.config.database import connect_to_mongo, close_mongo_connection
from app.routes import products, settings as settings_routes, auth, upload, reviews


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


app = FastAPI(
    title="Kalyani Resin Arts API",
    description="Backend API for Kalyani Resin Arts e-commerce showcase",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router, prefix="/api")
app.include_router(settings_routes.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(reviews.router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Welcome to Kalyani Resin Arts API",
        "docs": "/docs",
        "version": "1.0.0",
    }


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
