from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

load_dotenv()

from app.database import Base, engine
from app.routers import auth, medicine, sales, prediction, alert

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pharmacy Inventory System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# If you have a frontend build copied to backend/static, serve it:
# create a backend/static folder with the built frontend files if you want backend to serve static assets
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    # ignore if static directory is absent in some environments
    pass

app.include_router(auth.router)
app.include_router(medicine.router)
app.include_router(sales.router)
app.include_router(prediction.router)
app.include_router(alert.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Pharmacy Inventory System",
        version="1.0.0",
        description="API for managing pharmacy inventory and users.",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Minimal health endpoint for Railway / monitoring
@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}
