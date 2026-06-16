from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chatbot
import voice_engine
import fraud_detection
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SecureVote AI Service")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    language: str = "ur"
    voice_enabled: bool = True

class FraudRequest(BaseModel):
    hour: int
    attempts: int
    interval: int
    new_ip: int

@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "SecureVote AI"}

@app.post("/chatbot")
async def chat(request: ChatRequest):
    # Get text response
    response_text = chatbot.get_chatbot_response(request.message, request.language)
    
    # Generate voice if requested
    audio_base64 = None
    if request.voice_enabled:
        try:
            audio_base64 = await voice_engine.text_to_speech_base64(response_text, request.language)
        except Exception as e:
            print(f"TTS Error: {e}")
    
    return {
        "response": response_text,
        "audio": audio_base64
    }

@app.post("/fraud-check")
async def check_fraud(request: FraudRequest):
    try:
        data = {
            "hour": request.hour,
            "attempts": request.attempts,
            "interval": request.interval,
            "new_ip": request.new_ip
        }
        result = fraud_detection.predict_fraud(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Train model if not exists
    if not os.path.exists("fraud_model.pkl"):
        fraud_detection.train_initial_model()
        
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
