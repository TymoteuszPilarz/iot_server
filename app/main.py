from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

# Połączenie z MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.parking_system  # Baza danych
parking_spots_col = db.parking_spots  # Kolekcja dla miejsc parkingowych

# Model Pydantic do walidacji aktualizacji statusu miejsca parkingowego
class ParkingSpotStatus(BaseModel):
    parking_spot_id: str
    status: str  # "occupied" lub "free"

class User(BaseModel):
    username: str
    email: str

class ReservationRequest(BaseModel):
    username: str
    parking_spot_id: str
    action: str  # "reserve" lub "cancel"

@app.post("/create_user")
async def create_user(user: User):
    pass

@app.post("/reserve")
async def reserve_parking_spot(reservation: ReservationRequest):
    pass

# Endpoint do aktualizacji statusu miejsca parkingowego (wywoływany przez ESP32)
@app.post("/update_status")
async def update_parking_spot_status(spot_status: ParkingSpotStatus):
    # Znajdź miejsce parkingowe po jego ID w bazie danych
    # Jeśli miejsce parkingowe zostanie znalezione, zaktualizuj jego status (albo "occupied", albo "free")
    # Zwróć komunikat sukcesu z zaktualizowanym statusem
    pass

# Endpoint do sprawdzenia statusu wszystkich miejsc parkingowych (dla aplikacji)
@app.get("/parking_status")
async def get_parking_status():
    # Pobierz status wszystkich miejsc parkingowych z bazy danych
    # Zwróć listę miejsc parkingowych wraz z ich statusem ("occupied" lub "free")
    pass

# Endpoint do inicjalizacji miejsc parkingowych (wywoływany początkowo w celu zainicjowania miejsc)
@app.post("/initialize_spots")
async def initialize_spots():
    # Zainicjuj określoną liczbę miejsc parkingowych z domyślnym statusem "free"
    # Wstaw je do bazy danych w celu śledzenia
    pass