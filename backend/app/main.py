"""
Main FastAPI Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import diagnosis, adversarial, trajectory, community, vitals, risk, outbreak

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Neuro-Vitals: Predictive Health Intelligence System"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(diagnosis.router)
app.include_router(adversarial.router)
app.include_router(trajectory.router)
app.include_router(community.router)
app.include_router(vitals.router)
app.include_router(risk.router)
app.include_router(outbreak.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Neuro-Vitals API",
        "version": settings.VERSION,
        "docs": "/docs",
        "endpoints": {
            "diagnosis": "/api/diagnosis/analyze",
            "adversarial": "/api/adversarial/debate",
            "trajectory": "/api/trajectory/forecast",
            "community": "/api/community/heatmap",
            "vitals": {
                "save": "/api/save-vitals",
                "get": "/api/get-vitals/{user_email}",
                "latest": "/api/get-latest-vitals/{user_email}",
                "delete": "/api/delete-vitals/{user_email}",
                "health": "/api/vitals-health"
            },
            "risk": {
                "predict": "/api/risk/predict",
                "ocr": "/api/risk/ocr",
                "history": "/api/risk/history/{email}",
                "daily_log": "/api/risk/daily-log",
                "medical_record": "/api/risk/medical-record"
            },
            "outbreak": {
                "analyze": "/api/outbreak/analyze",
                "map": "/api/outbreak/map",
                "nearby": "/api/outbreak/map/nearby",
                "admin": "/api/outbreak/admin"
            }
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": settings.VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )