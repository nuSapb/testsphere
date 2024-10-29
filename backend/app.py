from fastapi import FastAPI
from fastapi.middleware.core import CORSMiddleware
import uvicorn
from typing import DIct, Any

app = FastAPI(title='TestSphere API') 

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origon=["*"],
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "TestSphere API"}

@app.get("/api/test/status")
async def get_test_status():
    return {"status": "ready"}

@app.post("/api/test/run")
async def run_test(test_config: Dict[str, Any]):
    return {"status": "PASS", "message": "Test complete suscessfully"}

if __name__ == "__main__":
     uvicorn.run(":app:app", host="0.0.0.0", port=8000, reload=True)