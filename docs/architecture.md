# Architecture — AR-DPP for VCU

## Overview

```
+------------------+       QR scan        +-----------------+
|  Physical VCU    |  ------------------> |  PICO 4 (Unity) |
|  (3D printed)    |   product_id         |                 |
+------------------+                      |  - QR tracking  |
                                          |  - DPPClient    |
                                          |  - Dashboard    |
                                          |  - Explosion    |
                                          +--------+--------+
                                                   |
                                                   | HTTP GET /dpp/{product_id}
                                                   v
                                          +-----------------+
                                          |   FastAPI       |
                                          |   backend       |
                                          |                 |
                                          |   data/*.json   |
                                          +-----------------+
```

## Layers

### Data layer — JSON files

- One file per VCU instance under `backend/data/{product_id}.json`.
- Conforms to `schema/dpp_schema.json` (CIRPASS-aligned).
- No database for prototype scope.

### Backend — FastAPI

- `GET /` — health check
- `GET /dpp` — list known product_ids
- `GET /dpp/{product_id}` — return DPP JSON
- Auto-generated OpenAPI docs at `/docs` (useful for thesis appendix).

### Frontend — Unity (PICO 4)

- `DPPClient.cs` — UnityWebRequest call to backend.
- `DPPModels.cs` — C# mirror of the JSON schema.
- `DPPDashboard.cs` — tab controller (Info + Explosion View for colloquium).
- `ExplosionController.cs` — DOTween animation of child components.
- `ComponentMetadata.cs` — DPP metadata attached to each 3D component.

## Phase 1 → Phase 2 expansion

| Layer    | Phase 1 (colloquium)             | Phase 2 (thesis)                                   |
|----------|----------------------------------|----------------------------------------------------|
| Data     | Identity + components + minimal env | + full BOM, real CO₂ data, hazardous flags        |
| Backend  | GET endpoints only               | + GPT-4o proxy endpoint for chatbot               |
| Frontend | Info + Explosion View tabs       | + Materials, Environmental, End-of-life, AI Assist |
| AR       | QR → world-anchored dashboard    | + component-level labels, gaze interaction        |

## Open decisions

- **QR library:** Vuforia (commercial, robust) vs ZXing (free, lighter). Decide before Apr 29 task.
- **JSON deserializer in Unity:** Newtonsoft.Json (handles nullables) — install via Unity Package Manager.
- **AR anchor strategy:** world anchor on QR detection vs continuous tracking. Likely world anchor for stability.
