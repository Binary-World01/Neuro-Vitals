"""
Vitals Router — Save and retrieve vitals data from Google Fit to Supabase.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import os

router = APIRouter()

# Supabase client
try:
    from supabase import create_client
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None
except Exception:
    supabase = None

class VitalsData(BaseModel):
    user_email: str
    steps: Optional[int] = 0
    heart_rate: Optional[int] = 0
    sleep_hours: Optional[float] = 0.0
    calories: Optional[int] = 0
    source: Optional[str] = "google_fit"
    recorded_at: Optional[datetime] = None

@router.get("/api/vitals-health")
async def vitals_health():
    return {"status": "ok", "supabase": supabase is not None}

@router.post("/api/save-vitals")

async def save_vitals(vitals: VitalsData):
    """Save vitals data from Google Fit to Supabase (upsert)"""
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    
    try:
        print(f"📥 [Supabase] Received vitals data for: {vitals.user_email}")
        
        # Prepare data for Supabase
        data = {
            "user_email": vitals.user_email,
            "steps": vitals.steps or 0,
            "heart_rate": vitals.heart_rate or 0,
            "sleep_hours": float(vitals.sleep_hours or 0),
            "calories": vitals.calories or 0,
            "source": vitals.source,
            "recorded_at": (vitals.recorded_at or datetime.now()).isoformat()
        }
        
        # UPSERT: Update if user_email exists, insert if not
        # First try to update
        update_result = supabase.table("user_vitals")\
            .update(data)\
            .eq("user_email", vitals.user_email)\
            .execute()
        
        # If no rows were updated, insert new record
        if not update_result.data:
            print(f"📝 [Supabase] No existing record, inserting new one...")
            result = supabase.table("user_vitals").insert(data).execute()
        else:
            print(f"🔄 [Supabase] Updated existing record for {vitals.user_email}")
            result = update_result
        
        print(f"✅ [Supabase] Data saved successfully!")
        
        return {
            "status": "success", 
            "message": "Vitals saved to Supabase",
            "data": result.data
        }
    
    except Exception as e:
        print(f"❌ [Supabase] Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))