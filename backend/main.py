"""
DPP API — FastAPI backend for the AR-DPP thesis prototype.

Serves Digital Product Passport JSON files for VCUs.
Storage: JSON files in ./data/, one per product_id.
"""
from pathlib import Path
import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DPP API",
    description="Digital Product Passport API for VCU AR prototype",
    version="0.1.0",
)

# CORS — open during prototype dev so Unity (any host) can call the API.
# Tighten before any public deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

DATA_DIR = Path(__file__).parent / "data"


@app.get("/")
def root():
    """Health check."""
    return {"status": "ok", "service": "DPP API", "version": "0.1.0"}


@app.get("/dpp/{product_id}")
def get_dpp(product_id: str):
    """Return the DPP JSON for the given product_id."""
    file_path = DATA_DIR / f"{product_id}.json"
    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"DPP not found for product_id: {product_id}",
        )
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


@app.get("/dpp")
def list_dpps():
    """List all known product_ids (filenames in data/)."""
    if not DATA_DIR.exists():
        return {"product_ids": []}
    return {
        "product_ids": [p.stem for p in DATA_DIR.glob("*.json")]
    }
