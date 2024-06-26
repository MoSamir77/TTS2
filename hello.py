import numpy as np
import sounddevice as sd
from TTS.api import TTS

print("hello Samiro")

tts =TTS( model_name="tts_models/en/jenny/jenny")
tts.tts_to_file(text="Hello,this is a test for converting text to speech system in a natural human likely voice, how can I help you?", 
                file_path="output.wav")

# Generate speech (returns numpy array)
# audio = 
#tts.tts("Hello, this is a test for converting text to speech system in a natural human likely voice, how can i help ")
#tts.tts_to_file(text="Hello, this is a test for converting text to speech system in a natural human likely voice, how can i help ")

# Play the audio
#sd.play(audio, samplerate=22050)
# sd.wait()  # Wait until the audio is done playing