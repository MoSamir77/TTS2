import os
from flask import Flask, request, send_file
from TTS.api import TTS
import tempfile

app = Flask(__name__)

# Initialize TTS with a specific model
tts = TTS(model_name="tts_models/en/jenny/jenny")

@app.route('/tts', methods=['POST'])
def text_to_speech():
    # Get the text from the request
    text = request.json.get('text', '')

    if not text:
        return {"error": "No text provided"}, 400

    # Generate speech and save it to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file_path = temp_file.name
        tts.tts_to_file(text=text, file_path=temp_file_path)

    # Send the audio file
    return send_file(temp_file_path, mimetype="audio/wav", as_attachment=True, download_name="output.wav")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
