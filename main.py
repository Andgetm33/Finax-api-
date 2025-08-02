from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les requêtes du front web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/assets")
def get_assets():
    return [
        {"name": "Apple", "symbol": "AAPL", "price": 189.56, "currency": "USD"},
        {"name": "Tesla", "symbol": "TSLA", "price": 255.41, "currency": "USD"},
        {"name": "Bitcoin", "symbol": "BTC", "price": 42300.75, "currency": "USD"},
        {"name": "Euro Stoxx 50", "symbol": "SX5E", "price": 4260.12, "currency": "EUR"}
    ]