from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import select

app = FastAPI()

#configuracion cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": select()}