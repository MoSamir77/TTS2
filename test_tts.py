import requests

url = "http://0.0.0.0:5000/tts"
payload = {"text": "Hello, this is a test."}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    print("Audio file saved as output.wav")
else:
    print(f"Request failed with status code {response.status_code}: {response.json()}")
