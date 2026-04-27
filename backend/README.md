# DPP Backend

FastAPI server that serves Digital Product Passport JSON files.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints

| Method | Path                  | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/`                   | Health check                         |
| GET    | `/dpp`                | List all known product_ids           |
| GET    | `/dpp/{product_id}`   | Get DPP JSON for a specific product  |
| GET    | `/docs`               | Interactive OpenAPI docs (Swagger UI)|

## Adding a new VCU

Drop a new JSON file into `data/` named `{product_id}.json`. It must conform to `../schema/dpp_schema.json`.

## Exposing to PICO 4 headset

The headset cannot reach `localhost` on your laptop. Two options:

1. **Same Wi-Fi:** start uvicorn with `--host 0.0.0.0` and use your laptop's LAN IP from Unity.
2. **ngrok:** `ngrok http 8000` and use the public URL in `DPPClient.baseUrl`.
