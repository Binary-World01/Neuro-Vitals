"""
Location Service – resolves the client's GPS or IP-based
geolocation for outbreak mapping.

Migrated from hackathon_project1/location_service.py.
"""

import logging
import httpx
from fastapi import Request

logger = logging.getLogger(__name__)


async def get_client_location(
    request: Request,
    gps_latitude: float | None = None,
    gps_longitude: float | None = None,
) -> dict:
    """Return a location dict with lat/lng/city/region/country/source."""
    try:
        # Prefer browser GPS when available
        if gps_latitude and gps_longitude:
            logger.info("GPS location: %s, %s", gps_latitude, gps_longitude)
            return {
                "latitude": float(gps_latitude),
                "longitude": float(gps_longitude),
                "city": "Unknown",
                "region": "Unknown",
                "country": "Unknown",
                "ip": request.client.host,
                "source": "gps",
            }

        # Fallback: IP geolocation
        client_ip = request.client.host
        logger.info("No GPS – using IP geolocation for %s", client_ip)

        if client_ip in ("127.0.0.1", "::1"):
            try:
                async with httpx.AsyncClient() as client:
                    ip_resp = await client.get("https://api.ipify.org?format=json")
                    if ip_resp.status_code == 200:
                        client_ip = ip_resp.json()["ip"]
            except Exception:
                pass

        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://ip-api.com/json/{client_ip}")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    return {
                        "latitude": data.get("lat"),
                        "longitude": data.get("lon"),
                        "city": data.get("city"),
                        "region": data.get("regionName"),
                        "country": data.get("country"),
                        "ip": client_ip,
                        "source": "ip_geolocation",
                    }
    except Exception as exc:
        logger.error("Location error: %s", exc)

    return {
        "latitude": None,
        "longitude": None,
        "city": None,
        "region": None,
        "country": None,
        "ip": request.client.host,
        "source": "unknown",
    }
