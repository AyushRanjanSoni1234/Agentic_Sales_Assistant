from fastapi import FastAPI
from pydantic import BaseModel
from graph import app

api = FastAPI()

class ChatRequest(BaseModel):
    message: str

@api.get("/")
def home():
    return {"status": "AI Sales Agent running"}

@api.post("/chat")
def chat(req: ChatRequest):
    result = app.invoke({"messages": req.message})
    return {"response": result["messages"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="127.0.0.1", port=8000)  # http://127.0.0.1:8000