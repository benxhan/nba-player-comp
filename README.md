# NBA Player Comparer — LangChain LLM Pipeline & Frontend/FastAPI integration

hello! langchain llm tool for nba player comparison in their reg. season vs post season.
added frontend w fastapi integration:

# Backend (Python)
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

# Frontend (React + Vite)
1. Install dependencies and start dev server:
```bash
cd frontend
npm install
npm run dev
```
The frontend expects the backend at `http://localhost:8000`
