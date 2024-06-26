import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from TTS.api import TTS
import tempfile

app = FastAPI()

# Initialize TTS with a specific model
tts = TTS(model_name="tts_models/en/jenny/jenny")

class TextRequest(BaseModel):
    text: str

@app.post("/tts")
async def text_to_speech(request: TextRequest):
    text = request.text

    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    # Generate speech and save it to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file_path = temp_file.name
        tts.tts_to_file(text=text, file_path=temp_file_path)

    # Send the audio file
    return FileResponse(temp_file_path, media_type="audio/wav", filename="output.wav")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
