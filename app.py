from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import json
from pyngrok import ngrok
import nest_asyncio
import uvicorn

app = FastAPI()
nest_asyncio.apply()

def read_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/index")
def get_data():
    data = read_data()
    return data

# Iniciar o túnel ngrok
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url}")

# Iniciar o servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)