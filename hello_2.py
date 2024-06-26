import subprocess

# Text to be converted to speech
text = "Hello, this is a test for converting text to speech using espeak-ng."

# Call espeak-ng from Python
subprocess.run(['espeak-ng', text])
