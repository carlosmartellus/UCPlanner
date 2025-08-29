from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .routes import user_routes
from .db.base import Base, engine, SessionLocal
from .controllers.user_controller import UserMainController
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="UCPlanner API")

Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "tauri://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
