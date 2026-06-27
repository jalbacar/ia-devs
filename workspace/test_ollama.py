import requests

url = "http://ollama:11434/api/generate"
payload = {
    "model": "smollm:135m",
    "prompt": "Say hello and introduce yourself in one sentence.",
    "stream": False
}

print("Sending request to Ollama...")
try:
    response = requests.post(url, json=payload, timeout=15)
    result = response.json()
    print("\n✅ Response from Ollama:")
    print(result.get("response", "No response content found."))
except Exception as e:
    print("\n❌ Error connecting to Ollama:", e)
