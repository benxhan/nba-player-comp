# nba reg. season vs playoffs — langchain LLM pipeline & frontend/fastAPI integration

hello! langchain llm tool for nba player comparison in their reg. season vs post season.
added frontend w fastapi integration:

# backend (python)
1. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the FastAPI app with Uvicorn:
```bash
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
```

API endpoints:
- `POST /api/player` with JSON `{ "name": "LeBron James" }`
- `GET /api/player/{name}`

# frontend (react + vite)
1. Install dependencies and start dev server:
```bash
cd frontend
npm install
npm run dev
```
the frontend expects the backend at `http://localhost:8000`
