
from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.routes import chat_routes, document_routes, user_routes

load_dotenv()

app = FastAPI()

app.include_router(chat_routes.router, prefix="/api")
app.include_router(document_routes.router, prefix="/api")
app.include_router(user_routes.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Hello from the Maryanne App Backend!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
